from antenna_lab.units import wavelength_m, C_MPS


def test_wavelength_basic():
    f = 300_000_000.0
    lam = wavelength_m(f)
    assert abs(lam - (C_MPS / f)) < 1e-12
