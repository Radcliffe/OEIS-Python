# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A291115

from sympy.core.cache import cacheit
from sympy import binomial, lcm, factorial as f
@cacheit
def b(n, m): return 0 if m>9 else (1 if m==9 else 0) if n==0 else sum([b(n - j, lcm(m, j))*binomial(n - 1, j - 1)*f(j - 1) for j in range(1, n + 1)])
def a(n): return sum([b(j, 1)*n**(n - j)*binomial(n - 1, j - 1) for j in range(n + 1)])
print([a(n) for n in range(26)]) # _Indranil Ghosh_, Aug 18 2017

