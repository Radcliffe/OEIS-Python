# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372912

from math import isqrt
def A372912(n): return isqrt(12*10**(n+1<<1)//49)%10 # _Chai Wah Wu_, Jul 08 2024

