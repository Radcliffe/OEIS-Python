# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A056811

from math import isqrt
from sympy import primepi
def a(n): return primepi(isqrt(n))
print([a(n) for n in range(1, 88)]) # _Michael S. Branicky_, Jan 19 2022

