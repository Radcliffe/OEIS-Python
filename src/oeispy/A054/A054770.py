# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A054770

from math import isqrt
def A054770(n): return (n+isqrt(5*n**2)>>1)+(n<<1)-1 # _Chai Wah Wu_, Aug 17 2022

