# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A035336

from math import isqrt
def A035336(n): return (n+isqrt(5*n**2)&-2)+n-1 # _Chai Wah Wu_, Aug 17 2022

