__all__ = []

globals()['_consts'] = _consts = {
    'pi': 3.14159,
    'h': 6.626e-34,  #j.s
    'c': 2.998e8, #m/s
    'G': 6.673e-11, #Nm^2/kg^2
    'e0': 8.854e-12, #F/m
    'u0': 1.257e-6, #H/m
    'e': 1.602e-19, #C
    'me': 9.109e-31, #kg
    'mp': 1.673e-27, #kg
    'a': 5.292e-11, #m
    'kB': 1.381e-23 # J/K
}
__all__.append('_consts')
for k, v in _consts.items():
    globals()[k] = v
    __all__.append(k)
