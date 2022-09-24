"""
Canonical Signed Digit Functions

Harnesser
License: GPL2
"""
from math import ceil, fabs, log


def to_csd(num: float, places: int) -> str:
    """Convert the argument `num` to a string in CSD Format.

    Original author: Harnesser
    <https://sourceforge.net/projects/pycsd/>
    License: GPL2

    Args:
        num (float): decimal value to be converted to CSD format
        places (int): number of fractional places

    Returns:
        str: containing the CSD value

    Examples:
        >>> to_csd(28.5, 2)
        '+00-00.+0'
        >>> to_csd(-0.5, 2)
        '0.-0'
    """

    # figure out binary range, special case for 0
    if num == 0.0:
        return "0"

    absnum = fabs(num)
    n = 0 if absnum < 1.0 else ceil(log(absnum * 1.5, 2))
    csd_str = "0" if absnum < 1.0 else ""
    pow2n = pow(2, n)
    while n > -places:
        if n == 0:
            csd_str += "."
        # convert the number
        pow2n_half = pow2n / 2
        d = 3 * num
        if d > pow2n:
            csd_str += "+"
            num -= pow2n_half
        elif d < -pow2n:
            csd_str += "-"
            num += pow2n_half
        else:
            csd_str += "0"
        pow2n = pow2n_half
        n -= 1

    return csd_str


def to_decimal(csd_str: str) -> float:
    """Convert the argument to a decimal number

    Original author: Harnesser
    <https://sourceforge.net/projects/pycsd/>
    License: GPL2

    Args:
        csd_str (str): string containing the CSD value

    Returns:
        float: decimal value of the CSD format

    Examples:
        >>> to_decimal("+00-00.+")
        28.5
        >>> to_decimal("0.-")
        -0.5
    """

    num: float = 0.0
    loc: int = 0
    for i, c in enumerate(csd_str):
        if c == "0":
            num *= 2.0
        elif c == "+":
            num = num * 2.0 + 1.0
        elif c == "-":
            num = num * 2.0 - 1.0
        elif c == ".":
            loc = i + 1
        else:
            pass  # ignore other characters

    if loc != 0:
        num /= pow(2.0, len(csd_str) - loc)

    return num


def to_decimal_i(csd_str: str) -> int:
    """Convert the argument to a decimal number

    Original author: Harnesser
    <https://sourceforge.net/projects/pycsd/>
    License: GPL2

    Args:
        csd_str (str): string containing the CSD value

    Returns:
        float: decimal value of the CSD format

    Examples:
        >>> to_decimal_i("+00-00")
        28
    """
    num: int = 0
    for c in csd_str:
        if c == "0":
            num *= 2
        elif c == "+":
            num = num * 2 + 1
        elif c == "-":
            num = num * 2 - 1
        else:
            pass  # ignore other characters
    return num


def to_csdfixed(num: float, nnz: int) -> str:
    """Convert the argument `num` to a string in CSD Format.

    Original author: Harnesser
    <https://sourceforge.net/projects/pycsd/>
    License: GPL2

    Args:
        num (float): decimal value to be converted to CSD format
        nnz (int): number of non-zerosssss

    Returns:
        str: containing the CSD value

    Examples:
        >>> to_csdfixed(28.5, 4)
        '+00-00.+'
        >>> to_csdfixed(-0.5, 4)
        '0.-'
    """

    if num == 0.0:
        return "0"

    absnum = fabs(num)
    n = 0 if absnum < 1.0 else ceil(log(absnum * 1.5, 2))
    csd_str = "0" if absnum < 1.0 else ""
    pow2n = pow(2.0, n)
    while n > 0 or (nnz > 0 and fabs(num) > 1e-100):
        if n == 0:
            csd_str += "."
        pow2n_half = pow2n / 2
        d = 3.0 * num
        if d > pow2n:
            csd_str += "+"
            num -= pow2n_half
            nnz -= 1
        elif d < -pow2n:
            csd_str += "-"
            num += pow2n_half
            nnz -= 1
        else:
            csd_str += "0"
        pow2n = pow2n_half
        n -= 1
        if nnz == 0:
            num = 0.0
    return csd_str


if __name__ == "__main__":
    import doctest

    doctest.testmod()
