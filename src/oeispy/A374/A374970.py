# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374970

from math import gcd
from sympy import divisors
def A374970(n): return sum(1 for d in divisors(n,generator=True) for x in range(1,d) for y in range(1,n//d) if gcd(x,y,d-x,n//d-y)==1) # _Chai Wah Wu_, Jul 26 2024

