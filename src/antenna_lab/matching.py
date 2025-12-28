from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class LMatchResult:
    topology: str  # "lowpass" or "highpass"
    series_type: str  # "L" or "C"
    series_value: float  # H or F
    shunt_type: str  # "C" or "L"
    shunt_value: float  # F or H
    q: float
    notes: str


def _reactance_to_L(x_ohm: float, freq_hz: float) -> float:
    # X_L = 2πfL
    return abs(x_ohm) / (2.0 * math.pi * freq_hz)


def _reactance_to_C(x_ohm: float, freq_hz: float) -> float:
    # X_C = 1/(2πfC)
    return 1.0 / (2.0 * math.pi * freq_hz * abs(x_ohm))


def synthesize_l_match(
    *,
    freq_hz: float,
    source_r_ohm: float,
    load_r_ohm: float,
    prefer_lowpass: bool = True,
) -> LMatchResult:
    """
    L-network synthesis for purely resistive load (engineering baseline).

    For R_load < R_source (common for quarter-wave monopole ≈36.5Ω into 50Ω),
    one can use:
      Q = sqrt(Rs/Rl - 1)
      X_series = Q * Rl
      X_shunt  = Rs / Q
    Component signs/topology chosen by 'prefer_lowpass' flag.

    This is a baseline tool: it does not model complex loads or parasitics.
    """
    if freq_hz <= 0:
        raise ValueError("freq_hz must be > 0")
    if source_r_ohm <= 0 or load_r_ohm <= 0:
        raise ValueError("impedances must be > 0")

    rs = float(source_r_ohm)
    rl = float(load_r_ohm)

    if math.isclose(rs, rl, rel_tol=1e-9):
        return LMatchResult(
            topology="none",
            series_type="L",
            series_value=0.0,
            shunt_type="C",
            shunt_value=0.0,
            q=0.0,
            notes="No match needed (Rs == Rl).",
        )

    # Normalize so formulas stay simple
    if rl < rs:
        q = math.sqrt(rs / rl - 1.0)
        x_series = q * rl
        x_shunt = rs / q
        notes = "Case: Rl < Rs (step-up to Rs)."
    else:
        q = math.sqrt(rl / rs - 1.0)
        x_series = q * rs
        x_shunt = rl / q
        notes = "Case: Rl > Rs (step-down to Rs)."

    # Choose component types by topology preference (baseline convention):
    # lowpass: series L, shunt C
    # highpass: series C, shunt L
    if prefer_lowpass:
        series_type = "L"
        shunt_type = "C"
        series_value = _reactance_to_L(x_series, freq_hz)
        shunt_value = _reactance_to_C(x_shunt, freq_hz)
        topology = "lowpass"
    else:
        series_type = "C"
        shunt_type = "L"
        series_value = _reactance_to_C(x_series, freq_hz)
        shunt_value = _reactance_to_L(x_shunt, freq_hz)
        topology = "highpass"

    return LMatchResult(
        topology=topology,
        series_type=series_type,
        series_value=series_value,
        shunt_type=shunt_type,
        shunt_value=shunt_value,
        q=q,
        notes=notes,
    )
