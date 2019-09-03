def El(L, I):
    """Returns the energy stored in an inductor."""
    return 0.5 * L * I ** 2

def Ec(C, V):
    """Returns the energy stored in a capacitor."""
    return 0.5 * C * V ** 2

def Pres(omega, Q, E):
    """Returns the energy dissipated by a resonator."""
    return omega * E / Q

def Qres(omega, E, P):
    """Returns quality factor of a resonator."""
    return omega * E / P
