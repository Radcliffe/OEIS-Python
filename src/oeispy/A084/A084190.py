# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A084190

from math import lcm
from sympy import divisors
def A084190(n): return lcm(*(d-1 for d in divisors(n,generator=True) if d > 1)) # _Chai Wah Wu_, Jun 25 2022

