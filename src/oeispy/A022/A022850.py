# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A022850

from math import isqrt
def A022850(n): return (m:=isqrt(k:=7*n*n))+int(k-m*(m+1)>=1) # _Chai Wah Wu_, Jul 31 2022

