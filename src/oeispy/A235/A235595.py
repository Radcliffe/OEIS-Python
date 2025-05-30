# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A235595

from sympy import binomial
from sympy.core.cache import cacheit
@cacheit
def b(n, h): return 1 if min(n, h)==0 else sum([binomial(n - 1, j - 1)*j*b(j - 1, h - 1)*b(n - j, h) for j in range(1, n + 1)])
def T(n, k): return b(n - 1, k - 1) - b(n - 1, k - 2)
for n in range(2, 13): print([T(n, d) for d in  range(1, n)]) # _Indranil Ghosh_, Aug 26 2017, after Maple code

