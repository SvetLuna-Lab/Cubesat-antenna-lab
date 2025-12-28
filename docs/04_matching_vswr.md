# 04 — Matching & VSWR (Baseline)

## Matching approach (v0.1.0)
- Use an L-network synthesis for resistive loads:
  - match `Z_load (≈R)` to source impedance (50 Ω)
- Provide both low-pass and high-pass forms; choose by config preference.

## VSWR/S11 notes
In v0.1.0 we treat VSWR as a validation target through measurement:
- Compute expected match components
- Verify using VNA (S11 curve and resonance shift)
- Update config correction knobs (VF/end-effect) based on observed results
