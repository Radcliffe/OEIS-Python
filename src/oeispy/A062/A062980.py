# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062980

from sympy.core.cache import cacheit
@cacheit
def a(n): return n*4 + 1 if n<2 else 6*n*a(n - 1) + sum(a(k)*a(n - k - 1) for k in range(1, n - 1))
print([a(n) for n in range(21)]) # _Indranil Ghosh_, Aug 09 2017

