# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A191898

from sympy.core.cache import cacheit
@cacheit
def T(n, k): return 0 if n<1 or k<1 else 1 if n==1 or k==1 else T(k, n) if k>n else T(k, (n - 1)%k + 1) if n>k else -sum([T(n, i) for i in range(1, n)])
for n in range(1, 21): print([T(k, n - k + 1) for k in range(1, n + 1)]) # _Indranil Ghosh_, Oct 23 2017

