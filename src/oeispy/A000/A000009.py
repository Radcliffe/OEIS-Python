# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000009

# uses A010815
from functools import lru_cache
from math import isqrt
@lru_cache(maxsize=None)
def A000009(n): return 1 if n == 0 else A010815(n)+2*sum((-1)**(k+1)*A000009(n-k**2) for k in range(1,isqrt(n)+1)) # _Chai Wah Wu_, Sep 08 2021

