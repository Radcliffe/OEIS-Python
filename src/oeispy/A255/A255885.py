# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A255885

from itertools import count
from sympy import isprime
def A255885(n):
    for b in count(1):
        if n == sum(1 for c in range(2,b+1) if not isprime(c) and pow(b,c-1,c**2) == 1):
            return b # _Chai Wah Wu_, May 18 2022

