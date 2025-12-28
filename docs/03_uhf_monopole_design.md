# 03 — UHF Quarter-wave Monopole (Baseline)

## Geometry (engineering baseline)
- Start from quarter-wave: L ≈ λ/4
- Apply correction knobs:
  - velocity factor (VF)
  - end-effect factor
  - trim margin (leave extra length for tuning)

## Ground reference
Monopole performance depends on the CubeSat chassis acting as a ground reference.
Document grounding points and keep feed layout consistent with the ICD.

## What v0.1.0 does (and does not)
- Does: reproducible sizing + matching baseline for resistive approximation
- Does not: full EM simulation or precise impedance prediction (planned later)
