# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000807

from sympy import binomial, bell
def a(n): return sum(binomial(2*n, k)*(-1)**k*bell(k)*bell(2*n - k) for k in range(2*n  + 1))
print([a(n) for n in range(21)]) # _Indranil Ghosh_, Sep 11 2017

