# 07 — Verification Plan (VNA/S11-ready)

## Bench verification
1) Continuity + mechanical inspection (pre-deploy)
2) VNA S11 sweep:
- resonance near target frequency
- acceptable return loss / VSWR in the planned channel band
3) Repeatability:
- same setup, same routing, consistent results

## Field sanity checks (optional)
- SDR receive test with known beacon source
- Doppler correction practice (ground pipeline rehearsal)

## Acceptance criteria (v0.1.0)
- Documented S11 curve and tuning notes
- Updated config knobs (VF/end-effect/trim) based on observations
