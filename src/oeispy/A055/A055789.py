# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055789

from math import comb, isqrt
def A055789(n): return comb(n,(m:=isqrt(n))+ int((n-m*(m+1)<<2)>=1)) # _Chai Wah Wu_, Jul 29 2022

