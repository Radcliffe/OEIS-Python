# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A088732

from itertools import accumulate, repeat
from sympy import isprime
def A088732(n): return next(m for m in accumulate(repeat(n+1),initial=(n<<1)+1) if isprime(m)) # _Chai Wah Wu_, Aug 02 2023

