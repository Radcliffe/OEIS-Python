# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A071764

from math import isqrt
def A071764(n): return ((s:=isqrt(n-1))*(s-1)+1+(n>>1)+(n*(n+1)>>1)>>1)-sum((n-1)//k for k in range(1,s+1)) if n else 1 # _Chai Wah Wu_, Oct 31 2023

