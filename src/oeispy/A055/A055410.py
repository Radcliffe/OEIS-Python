# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055410

from math import isqrt
def A055410(n): return 1+((-(s:=n**2)*(n+1)+sum((q:=s//k)*((k<<1)+q+1) for k in range(1,n+1))&-1)<<2)+(((t:=isqrt(m:=s>>2))**2*(t+1)-sum((q:=m//k)*((k<<1)+q+1) for k in range(1,t+1))&-1)<<4) # _Chai Wah Wu_, Jun 24 2024

