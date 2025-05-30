# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343493

from functools import lru_cache
from sympy import divisors
@lru_cache(maxsize=None)
def A343493(n): return 1-sum(A343493(d-1) for d in divisors(n) if d < n) # _Chai Wah Wu_, Apr 17 2021

