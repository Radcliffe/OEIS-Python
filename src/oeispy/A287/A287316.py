# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287316

from math import comb
from functools import lru_cache
@lru_cache(maxsize=None)
def A(n,k):
    if k <= 0:
        return 0**n
    return sum(A(i,k-1)*comb(n,i)**2 for i in range(n+1))
N = 50
i = 0
for n in range(N+1):
    for k in range(n+1):
        print(i, A(k,n-k))
        i += 1
# _Jeremy Tan_, Dec 10 2021

