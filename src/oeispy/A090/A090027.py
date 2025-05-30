# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A090027

from functools import lru_cache
@lru_cache(maxsize=None)
def A090027(n):
    if n == 0:
        return 0
    c, j = 1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A090027(k1)
        j, k1 = j2, n//j2
    return (n+1)**5-c+31*(j-n-1) # _Chai Wah Wu_, Mar 30 2021

