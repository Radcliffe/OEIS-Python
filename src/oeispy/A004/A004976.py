# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A004976

from math import isqrt
def A004976(n): return (isqrt(20*n**2)>>1)+(n<<1) # _Chai Wah Wu_, Aug 17 2022

