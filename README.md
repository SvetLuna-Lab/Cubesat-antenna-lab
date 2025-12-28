# CubeSat Antenna Lab — Antennas-first (1U)
[![CI](https://github.com/SvetLuna-Lab/cubesat-antenna-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/SvetLuna-Lab/cubesat-antenna-lab/actions/workflows/ci.yml)

Antenna-first engineering lab for a 1U CubeSat.
This repository builds a reproducible antenna subsystem baseline and keeps it honest with tests and CI:
**sizing → matching/VSWR → trade-offs → ICD → verification plan**.

**Baseline (v0.1.0):** Deployable UHF quarter-wave monopole + matching + ICD + verification plan + CI.  
**Extension path:** S-band microstrip patch (prepared as a modular profile).

---

## Why this matters
A CubeSat can be perfect on paper and still go silent in orbit if the antenna system is treated as a late integration detail.
This project makes the antenna a first-class system: geometry and RF constraints shape the mission link budget, not the other way around.

## Engineering signals (what this repo demonstrates)
- **Reproducibility:** versioned configs drive calculations (`configs/*.yaml`).
- **Traceability:** assumptions → equations → outputs (no hidden magic numbers).
- **Verification mindset:** ICD + verification plan included (VNA/S11-ready).
- **Determinism:** tests validate sizing/matching sanity.
- **CI discipline:** lint + tests on every push/PR.

## Scope (v0.1.0)
- UHF monopole parametric sizing (frequency → wavelength → physical length).
- Matching network synthesis (L-network baseline, practical losses accounted as parameters).
- VSWR/S11 approximations (engineering-level, documented assumptions).
- Documentation pack: requirements, trade study, ICD, verification plan.
- CI: pytest + ruff + GitHub Actions.

## Repository structure
- `configs/` — antenna design profiles (UHF baseline, S-band stub).
- `docs/` — requirements, trade study, monopole design, matching/VSWR, ICD, verification plan.
- `src/` — sizing + matching utilities.
- `tests/` — deterministic checks for sizing/matching.
- `.github/workflows/` — CI pipeline.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

## Integration with COMMS-first

This repo is designed to plug into your COMMS-first link budget parameters:

- tx_antenna_gain_dbi

- tx_line_loss_db

- misc_losses_db (deployment/polarization/implementation losses)

See also: CubeSat COMMS-first baseline repo (link in your profile / Featured).

## Roadmap

- v0.1.1: sensitivity sweeps (length tolerances, losses, frequency offsets).

- v0.2.0: alternative UHF candidate (turnstile / crossed dipoles) + updated trade study.

- v0.3.0: S-band patch becomes a real design branch (not just stub), with verification steps.

## Regulatory & safety note

Frequencies and RF parameters may be placeholders. Real hardware work must comply with regulations and proper RF safety practices.

pytest -q
ruff check src tests
