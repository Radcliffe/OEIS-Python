# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345683

from math import factorial, isqrt
def A345683(n): return (m:=factorial(n))*(n-1)+m//n+sum((q:=n//k)*(m//k-m//(k-1))+m//q for k in range(2,isqrt(n)+1)) # _Chai Wah Wu_, Oct 27 2023

