# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361982

from functools import lru_cache
@lru_cache(maxsize=None)
def A361982(n):
    if n <= 1:
        return 1
    c, j = 1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (((j2<<1)-1 if j2&1 else -(j2<<1)+1)+(-(j<<1)+1 if j&1 else (j<<1)-1)>>2)*A361982(k1)
        j, k1 = j2, n//j2
    return c+((-(n<<1)-1 if n&1 else (n<<1)+1)+(-(j<<1)+1 if j&1 else (j<<1)-1)>>2) # _Chai Wah Wu_, Apr 02 2023

