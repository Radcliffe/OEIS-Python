# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001670

from math import isqrt
def A001670(n): return (m:=isqrt(n))+int((n-m*(m+1)<<2)>=1)<<1 # _Chai Wah Wu_, Jul 29 2022

