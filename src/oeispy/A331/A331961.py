# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A331961

from math import isqrt
def A331961(n): return next(m for m in (k**2 for k in range(isqrt(n),-1,-1)) if n&m==m) # _Chai Wah Wu_, Aug 22 2023

