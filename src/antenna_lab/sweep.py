from __future__ import annotations

import argparse
from dataclasses import asdict
from pathlib import Path

import numpy as np
import yaml

from antenna_lab.monopole import MonopoleDesign
from antenna_lab.matching import synthesize_l_match


def load_yaml(path: str | Path) -> dict:
    p = Path(path)
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def run_sweep(cfg_path: str, n: int = 5, span_pct: float = 2.0) -> list[dict]:
    cfg = load_yaml(cfg_path)

    ant = cfg["antenna"]
    sys = cfg.get("system", {})

    f0 = float(ant["freq_hz"])
    span = (span_pct / 100.0) * f0
    freqs = np.linspace(f0 - span, f0 + span, num=n)

    out: list[dict] = []
    for f in freqs:
        design = MonopoleDesign(
            freq_hz=float(f),
            velocity_factor=float(ant.get("velocity_factor", 1.0)),
            end_effect=float(ant.get("end_effect", 1.0)),
            trim_margin_m=float(ant.get("trim_margin_m", 0.0)),
        )

        match = synthesize_l_match(
            freq_hz=float(f),
            source_r_ohm=float(sys.get("source_impedance_ohm", 50.0)),
            load_r_ohm=float(sys.get("estimated_load_r_ohm", 36.5)),
            prefer_lowpass=bool(sys.get("prefer_lowpass", True)),
        )

        out.append(
            {
                "freq_hz": float(f),
                "quarter_wave_m": float(design.quarter_wave_m),
                "recommended_cut_length_m": float(design.recommended_cut_length_m),
                "match": asdict(match),
            }
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Antenna Lab sweep (baseline).")
    ap.add_argument("--config", required=True, help="Path to YAML config.")
    ap.add_argument("--n", type=int, default=5, help="Number of sweep points.")
    ap.add_argument("--span-pct", type=float, default=2.0, help="Sweep span around f0 in percent.")
    args = ap.parse_args()

    rows = run_sweep(args.config, n=args.n, span_pct=args.span_pct)
    for r in rows:
        f_mhz = r["freq_hz"] / 1e6
        L_cm = r["quarter_wave_m"] * 100.0
        cut_cm = r["recommended_cut_length_m"] * 100.0
        m = r["match"]
        print(
            f"{f_mhz:9.3f} MHz | Lq={L_cm:6.2f} cm | cut={cut_cm:6.2f} cm | "
            f"{m['topology']} series{m['series_type']}={m['series_value']:.3e} "
            f"shunt{m['shunt_type']}={m['shunt_value']:.3e} Q={m['q']:.3f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
