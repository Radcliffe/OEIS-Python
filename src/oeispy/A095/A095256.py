# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A095256

from math import isqrt
def A095256(n): return -(s:=isqrt(m:=10**n))**2+(sum(m//k for k in range(1,s+1))<<1)-(n+1)**2 # _Chai Wah Wu_, Oct 23 2023

