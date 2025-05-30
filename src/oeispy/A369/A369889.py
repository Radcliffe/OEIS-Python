# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369889

from math import prod
from sympy import mobius, integer_nthroot, primefactors
def A369889(n):
    def f(x): return n+x-sum(mobius(k)*(x//k**3) for k in range(1, integer_nthroot(x,3)[0]+1))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return prod(p+1 for p in primefactors(m)) # _Chai Wah Wu_, Aug 12 2024

