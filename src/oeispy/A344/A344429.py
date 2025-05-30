# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344429

from functools import lru_cache
from math import comb
from sympy import bernoulli
@lru_cache(maxsize=None)
def faulhaber(n,p):
    """ Faulhaber's formula for calculating Sum_{k=1..n} k^p
        requires sympy version 1.12+ where bernoulli(1) = 1/2
    """
    return sum(comb(p+1,k)*bernoulli(k)*n**(p-k+1) for k in range(p+1))//(p+1)
@lru_cache(maxsize=None)
def A344429(n,m=None):
    if n <= 1:
        return 1
    if m is None:
        m=n
    c, j = 1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (faulhaber(j-1,m)-faulhaber(j2-1,m))*A344429(k1,m)
        j, k1 = j2, n//j2
    return c+faulhaber(j-1,m)-faulhaber(n,m) # _Chai Wah Wu_, Nov 02 2023

