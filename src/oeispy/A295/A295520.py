# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A295520

from itertools import count
from sympy import isprime
def A295520(n): return next(k for k in count(0) if isprime(n^k)) # _Chai Wah Wu_, Aug 23 2023

