# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A101642

from math import isqrt
def A101642(n): return 3*(n+1+isqrt(5*(n+1)**2)>>1)+(n<<1)-3 # _Chai Wah Wu_, Aug 29 2022

