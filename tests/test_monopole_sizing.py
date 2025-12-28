from antenna_lab.monopole import MonopoleDesign
from antenna_lab.units import wavelength_m


def test_quarter_wave_sizing_nominal():
    f = 300_000_000.0
    d = MonopoleDesign(freq_hz=f, velocity_factor=1.0, end_effect=1.0, trim_margin_m=0.0)

    expected = 0.25 * wavelength_m(f)
    assert abs(d.quarter_wave_m - expected) < 1e-9


def test_recommended_cut_includes_trim():
    f = 437_500_000.0
    d = MonopoleDesign(freq_hz=f, velocity_factor=0.95, end_effect=0.97, trim_margin_m=0.02)
    assert d.recommended_cut_length_m > d.quarter_wave_m
