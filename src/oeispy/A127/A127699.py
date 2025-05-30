# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A127699

from functools import lru_cache
from math import lcm
from sympy import reduced_totient
@lru_cache(maxsize=None)
def A127699(n): return 1 if n == 1 else lcm(n, A127699(reduced_totient(n))) # _Chai Wah Wu_, Jan 03 2023

