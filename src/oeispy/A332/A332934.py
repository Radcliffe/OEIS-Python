# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A332934

from math import isqrt
from sympy import divisors
def A332934(n): return sum((m:=isqrt(r:=d**3))+int(r-m*(m+1)>=1) for d in divisors(n,generator=True)) # _Chai Wah Wu_, Aug 03 2022

