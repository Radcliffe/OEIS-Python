# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350124

from math import isqrt
def A350124(n): return (-(s:=isqrt(n))**4*(s+1)*(2*s+1) + sum((q:=n//k)*(k*(3*(k-1))+q*(k*(9*(k-1))+q*(k*(12*k-6)+2)+3)+1) for k in range(1,s+1)))//6 # _Chai Wah Wu_, Oct 21 2023

