# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A019446

from math import isqrt
def A019446(n): return (n+isqrt(5*n**2)>>1)-n+1 # _Chai Wah Wu_, Aug 09 2022

