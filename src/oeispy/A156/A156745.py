# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A156745

from math import isqrt
def A156745(n): return n-(s:=isqrt(n))**2+(sum(n//k for k in range(1,s+1))<<1) # _Chai Wah Wu_, Oct 23 2023

