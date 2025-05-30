# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A290638

from sympy.core.cache import cacheit
from sympy import denom, Rational
@cacheit
def g(i, j): return Rational(i) if j==0 else g(i, j - 1)/g(i + 2**(j - 1), j - 1)
def a(n): return denom(g(1, n))
print([a(n) for n in range(12)]) # _Indranil Ghosh_, Aug 09 2017, after Maple code

