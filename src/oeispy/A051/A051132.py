# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A051132

from math import isqrt
def A051132(n): return 1+(sum(isqrt(k*((n<<1)-k)-1) for k in range(1,n+1))<<2) if n else 0 # _Chai Wah Wu_, Feb 12 2025

