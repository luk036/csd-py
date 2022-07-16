import pytest

from csd_py.csd import to_csd, to_decimal


@pytest.mark.randomize(d=int, ncalls=5)
def test_csd(d):
    f = float(d)
    assert f == to_decimal(to_csd(f, 2))
