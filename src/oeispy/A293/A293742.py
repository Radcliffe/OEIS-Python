# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A293742

from sympy.core.cache import cacheit
from sympy import binomial
@cacheit
def g(n): return 1 if n<2 else g(n - 1) + sum(g(k)*g(n - k - 2) for k in range(n - 1))
@cacheit
def b(n, i): return 1 if n==0 else 0 if i<1 else sum(b(n - i*j, i - 1)*binomial(g(i), j) for j in range(n//i + 1))
def a(n): return b(n, n)
print([a(n) for n in range(36)]) # _Indranil Ghosh_, Oct 15 2017

