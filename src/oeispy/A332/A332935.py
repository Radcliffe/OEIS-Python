# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A332935

from math import isqrt
from sympy import divisors
def A332935(n): return sum(1+isqrt(d**3-1) for d in divisors(n,generator=True)) # _Chai Wah Wu_, Aug 03 2022

