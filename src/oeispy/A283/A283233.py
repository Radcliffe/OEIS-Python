# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A283233

from math import isqrt
def A283233(n): return (n+isqrt(5*n**2))&-2 # _Chai Wah Wu_, Aug 10 2022

