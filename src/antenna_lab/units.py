from __future__ import annotations

import math

C_MPS = 299_792_458.0


def wavelength_m(freq_hz: float) -> float:
    if freq_hz <= 0:
        raise ValueError("freq_hz must be > 0")
    return C_MPS / freq_hz


def db_to_linear(db: float) -> float:
    return 10.0 ** (db / 10.0)


def linear_to_db(x: float) -> float:
    if x <= 0:
        raise ValueError("x must be > 0")
    return 10.0 * math.log10(x)
