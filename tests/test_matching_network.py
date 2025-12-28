from antenna_lab.matching import synthesize_l_match


def test_l_match_components_positive():
    res = synthesize_l_match(
        freq_hz=437_500_000.0,
        source_r_ohm=50.0,
        load_r_ohm=36.5,
        prefer_lowpass=True,
    )
    assert res.topology in ("lowpass", "highpass", "none")
    assert res.series_value >= 0.0
    assert res.shunt_value >= 0.0
    assert res.q >= 0.0


def test_no_match_when_equal():
    res = synthesize_l_match(freq_hz=100e6, source_r_ohm=50.0, load_r_ohm=50.0)
    assert res.topology == "none"
    assert res.series_value == 0.0
    assert res.shunt_value == 0.0
