# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A008292

from sympy import binomial
def T(n, k): return sum([(-1)**j*(k - j)**n*binomial(n + 1, j) for j in range(k + 1)])
for n in range(1, 11): print([T(n, k) for k in range(1, n + 1)]) # _Indranil Ghosh_, Nov 08 2017

