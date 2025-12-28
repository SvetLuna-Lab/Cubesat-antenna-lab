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

## Engineering signals
- **Reproducibility:** versioned configs drive calculations (`configs/*.yaml`).
- **Traceability:** assumptions → equations → outputs (no hidden magic numbers).
- **Verification mindset:** ICD + verification plan included (VNA/S11-ready).
- **Determinism:** tests validate sizing/matching sanity.
- **CI discipline:** lint + tests on every push/PR.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]

pytest -q
ruff check src tests
python -m antenna_lab.sweep --config configs/uhf_monopole.yaml --n 5
```

## Integration with COMMS-first

This repo is designed to feed COMMS-first link budgets:

- tx_antenna_gain_dbi

- tx_line_loss_db

- misc_losses_db (deployment/polarization/implementation losses)

## Regulatory & safety note

Frequencies and RF parameters may be placeholders. Real hardware work must comply with regulations and proper RF safety practices.
