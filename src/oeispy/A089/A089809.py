# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A089809

from math import isqrt
def A089809(n): return ((n+isqrt(5*n**2))&1)^1 # _Chai Wah Wu_, Aug 17 2022

