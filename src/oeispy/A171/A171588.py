# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A171588

from math import isqrt
def A171588(n): return 1+isqrt(n**2>>1)-isqrt((n+1)**2>>1) # _Chai Wah Wu_, May 24 2025

