# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A017912

from math import isqrt
def A017912(n): return isqrt(1<<n)+1 if n&1 else 1<<(n>>1) # _Chai Wah Wu_, Jul 26 2022

