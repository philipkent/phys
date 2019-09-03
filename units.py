_bare_units = {
    'A': 1,
    'F': 1,
    'V': 1,
    'W': 1,
    'H': 1,
    'Hz': 1,
    'm': 1,
    's': 1,
    'g': 1e-3,
    'eV': 1.602e-19
}

_bare_prefixes = {
    '': 1,
    'Y': 1e24,
    'Z': 1e21,
    'E': 1e18,
    'P': 1e15,
    'T': 1e12,
    'G': 1e9,
    'M': 1e6,
    'k': 1e3,
    'h': 1e2,
    'da': 1e1,
    'd': 1e-1,
    'c': 1e-2,
    'm': 1e-3,
    'u': 1e-6,
    'n': 1e-9,
    'p': 1e-12,
    'f': 1e-15,
    'a': 1e-18,
    'z': 1e-21,
    'y': 1e-24
}
__all__ = []
globals()['_units'] = {}
globals()['_prefixes'] = {}
__all__.append('_units')
__all__.append('_prefixes')

for kk, vv in _bare_prefixes.items():
    globals()['_prefixes'][kk] = vv
    for k, v in _bare_units.items():
        name = "{0}{1}".format(kk, k)
        value = v*vv
        globals()['_units'][name] = value
        globals()[name] = value
        __all__.append(name)


