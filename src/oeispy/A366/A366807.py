# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366807

from math import isqrt
from sympy import primepi, mobius, primefactors
def A366807(n):
    def f(x): return n+1+primepi(x)+x-sum(mobius(k)*(x//k**2) for k in range(1, isqrt(x)+1))
    m, k = n+1, f(n+1)
    while m != k:
        m, k = k, f(k)
    return m*min(primefactors(m)) # _Chai Wah Wu_, Aug 02 2024

