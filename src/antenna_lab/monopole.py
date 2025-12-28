from __future__ import annotations

from dataclasses import dataclass

from antenna_lab.units import wavelength_m


@dataclass(frozen=True)
class MonopoleDesign:
    freq_hz: float
    velocity_factor: float = 1.0
    end_effect: float = 1.0
    trim_margin_m: float = 0.0

    @property
    def quarter_wave_m(self) -> float:
        # Engineering baseline: L = (λ/4) * VF * end_effect
        lam = wavelength_m(self.freq_hz)
        return 0.25 * lam * self.velocity_factor * self.end_effect

    @property
    def recommended_cut_length_m(self) -> float:
        # Leave some length for trimming during tuning
        return self.quarter_wave_m + self.trim_margin_m


def radiation_resistance_ohm() -> float:
    # Order-of-magnitude for quarter-wave monopole over an ideal ground plane
    return 36.5
