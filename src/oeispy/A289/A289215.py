# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A289215

from mpmath import *
mp.dps=100
def a(n): return int(fac(n)*laguerre(n, 0, -9))
print([a(n) for n in range(21)]) # _Indranil Ghosh_, Jul 04 2017

