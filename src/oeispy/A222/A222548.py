# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A222548

from math import isqrt
def A222548(n): return -(s:=isqrt(n))**3 + sum((q:=n//k)*((k<<1)+q-1) for k in range(1,s+1)) # _Chai Wah Wu_, Oct 21 2023

