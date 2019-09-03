from .units import *


def scaled(val, scale=1, ndecimals=None):
    val = val / scale
    if ndecimals is not None:
        val = round(val, ndecimals)
    return val


def uprint(val, unit=None, ndecimals=None, append=""):
    if unit is not None:
        print("{0} {1}{2}".format(scaled(val, _units[unit], ndecimals), unit, append))
    else:
        print("{0}{1}".format(scaled(val, 1, ndecimals), append))
