# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A177970

from sympy import binomial
def T(m, n): return (2*n + 1)*binomial(2*m + 1 + 2*n, 2*m) - 2*n - 2*m
for n in range(11): print([T(m, n - m) for m in range(n + 1)]) # _Indranil Ghosh_, Jul 06 2017

