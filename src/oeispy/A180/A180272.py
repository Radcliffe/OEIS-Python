# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180272

from math import comb, isqrt
def A180272(n): return comb(n,(isqrt(n+1<<3)+1>>1)-1) # _Chai Wah Wu_, Oct 17 2022

