# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A288386

from sympy.core.cache import cacheit
from sympy import binomial
@cacheit
def b(n, k, j): return 1 if j==n else sum(sum(binomial(i, m)*binomial(j - 1, i - 1 - m) for m in range(max(k, i - j), i))*b(n - j, k, i) for i in range(1, n - j + 1))
@cacheit
def T(n, k): return 1 if n==0 else sum(b(n, k, j) for j in range(k, n + 1))
for n in range(16): print([T(n, k) for k in range(n + 1)]) # _Indranil Ghosh_, Aug 09 2017

