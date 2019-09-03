from phys.consts import *
import math


def PlanckDist(E, T):
    return 1 / (math.exp(E / (kB * T)) - 1)


def PlanckSpec(f, cn, T):
    """Returns the Planck energy specturm of energy per unit volume per unit frequency."""
    return PlanckDist(h * f, T) * (8 * pi * h * f**3) / cn**3
