# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A291977

from sympy.core.cache import cacheit
from sympy import binomial
@cacheit
def eulerian1(n, k): return 1 if k==0 else 0 if k==n else eulerian1(n - 1, k)*(k + 1) + eulerian1(n - 1, k - 1)*(n - k)
def T(n, k): return sum([(-1)**(k - j)*eulerian1(n, j)*binomial(n - j, n - k) for j in range(n + 1)])
for n in range(10): print([T(n, k) for k in range(n + 1)]) # _Indranil Ghosh_, Sep 11 2017

