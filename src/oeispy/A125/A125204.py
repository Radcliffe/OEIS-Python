# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A125204

from sympy.core.cache import cacheit
@cacheit
def a(n): return n if n<2 else a(n - 1) + a(a(n - 1)%n)
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Aug 07 2017

