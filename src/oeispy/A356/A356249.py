# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356249

from math import isqrt
def A356249(n): return -(s:=isqrt(n))**5*(s+1)**2 + sum((q:=n//k)**2*(k*(3*(k-1))+q*(k*(k*(4*k+6)-6)+q*(k*(3*(k-1))+1)+2)+1) for k in range(1,s+1))>>2 # _Chai Wah Wu_, Oct 21 2023

