# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A089910

from math import isqrt
def A089910(n): return (n+isqrt(5*n**2)&-2)+n+1 # _Chai Wah Wu_, Aug 29 2022

