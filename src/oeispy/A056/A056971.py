# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A056971

from functools import lru_cache
from math import comb
@lru_cache(maxsize=None)
def A056971(n):
    if n<=1: return 1
    h = (n+1).bit_length()-2
    b = (1<<h)-1
    r = n-1-(b<<1)
    r1 = r-(r//(b+1))*(r-b-1)
    r2 = r-r1
    return comb(n-1,b+r1)*A056971(b+r1)*A056971(b+r2) # _Chai Wah Wu_, May 06 2024

