# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A134862

from math import isqrt
def A134862(n): return 5*(n+isqrt(5*n**2)>>1)+3*n # _Chai Wah Wu_, Aug 10 2022

