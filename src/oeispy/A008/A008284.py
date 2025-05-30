# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A008284

from functools import lru_cache
@lru_cache(maxsize=None)
def A008284_T(n,k):
    if k==n or k==1: return 1
    if k>n: return 0
    return A008284_T(n-1,k-1)+A008284_T(n-k,k) # _Chai Wah Wu_, Sep 21 2023

