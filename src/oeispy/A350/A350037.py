# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350037

from math import isqrt
def A350037(n): return pow(n,2,(m:=isqrt(n))+int(4*n>=(2*m+1)**2)) # _Chai Wah Wu_, Jan 10 2022

