# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A256532

from math import isqrt
def A256532(n): return n**3+n*((s:=isqrt(n))**2*(s+1)-sum((q:=n//k)*((k<<1)+q+1) for k in range(1,s+1))>>1) # _Chai Wah Wu_, Oct 22 2023

