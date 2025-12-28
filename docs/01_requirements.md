# 01 — Requirements (Antenna-first)

## Mission driver
Close the radio link with margins. Antenna performance and integration constraints are treated as primary design inputs.

## Baseline target (v0.1.0)
- Band: UHF (placeholder frequency)
- Antenna: deployable quarter-wave monopole baseline
- Goal: reproducible sizing + matching baseline + verification plan (VNA/S11-ready)

## Constraints (1U realities)
- Volume: strict, deployment must be reliable
- Power: TX power limited → antenna efficiency matters
- Orientation uncertainty: design must tolerate attitude variations (coverage trade-offs)
- Integration: feedline routing, grounding, EMC/ESD must be documented (ICD)

## Deliverables (portfolio-grade)
- Calculations in code (configs versioned)
- Trade study of candidates (at least 2–3)
- ICD (mechanical + electrical interface)
- Verification plan (bench + field sanity checks)
