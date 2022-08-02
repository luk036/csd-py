import pytest

from csd_py.csd import to_csd, to_decimal


def test_csd():
    f = 1234.0
    assert f == to_decimal(to_csd(f, 2))
