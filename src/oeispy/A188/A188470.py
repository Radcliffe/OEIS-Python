# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A188470

from math import isqrt
def A188470(n): return 7-(n+isqrt(5*n**2)>>1)+(n-1+isqrt(5*(n-5)**2)>>1) if n>5 else int(n<5) # _Chai Wah Wu_, Aug 10 2022

