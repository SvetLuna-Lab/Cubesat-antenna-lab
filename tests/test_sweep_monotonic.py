from antenna_lab.monopole import MonopoleDesign


def test_quarter_wave_decreases_with_frequency():
    d1 = MonopoleDesign(freq_hz=400e6)
    d2 = MonopoleDesign(freq_hz=450e6)
    assert d2.quarter_wave_m < d1.quarter_wave_m
