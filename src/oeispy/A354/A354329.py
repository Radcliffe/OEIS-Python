# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354329

from math import isqrt
def A354329(n): return (m:=isqrt(n*(n*(n + 3) + 2)//3))*(m+1)>>1 # _Chai Wah Wu_, Jul 15 2022

