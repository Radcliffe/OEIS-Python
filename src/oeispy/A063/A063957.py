# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063957

from math import isqrt
def A063957(n): return (a:=(n<<1)-1)+(m:=isqrt(k:=a**2<<1)>>1)+int(((m<<1)+1)**2<k) # _Chai Wah Wu_, Feb 11 2025

