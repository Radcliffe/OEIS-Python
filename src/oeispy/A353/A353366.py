# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353366

from functools import lru_cache
from sympy import divisors
@lru_cache(maxsize=None)
def A353366(n): return 1 if n==1 else -sum(((1+(m:=d>>(~d&d-1).bit_length())>>(m+1&-m-1).bit_length())+1)*A353366(n//d) for d in divisors(n,generator=True) if d>1) # _Chai Wah Wu_, Jan 04 2024

