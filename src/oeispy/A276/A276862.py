# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A276862

from math import isqrt
def A276862(n): return 1-isqrt(m:=n*n<<1)+isqrt(m+(n<<2)+2) # _Chai Wah Wu_, Aug 03 2022

