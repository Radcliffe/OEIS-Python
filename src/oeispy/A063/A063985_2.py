# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063985

from functools import lru_cache
@lru_cache(maxsize=None)
def A063985(n): # based on second formula in A018805
    if n == 0:
        return 0
    c, j = 0, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*(k1*(k1+1)-2*A063985(k1)-1)
        j, k1 = j2, n//j2
    return (2*n+c-j)//2 # _Chai Wah Wu_, Mar 24 2021

