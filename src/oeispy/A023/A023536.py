# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A023536

from math import comb, isqrt
def A023536(n): return comb(n+2,2)-sum(isqrt((k<<3)+1)-1>>1 for k in range(1,n+2)) # _Chai Wah Wu_, Feb 27 2025

