# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A003622

from math import isqrt
def A003622(n): return (n+isqrt(5*n**2)>>1)+n-1 # _Chai Wah Wu_, Aug 11 2022

