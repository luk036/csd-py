from math import sqrt

from hypothesis import given
from hypothesis.strategies import integers

from csd_py.csd import to_csd, to_csd_i, to_decimal, to_decimal_i


def test_csd():
    f = 1234.5
    assert f == to_decimal(to_csd(f, 2))


@given(integers())
def test_csd_i(number):
    num = int(sqrt(abs(number)))  # don't too large
    assert num == to_decimal_i(to_csd_i(num))
