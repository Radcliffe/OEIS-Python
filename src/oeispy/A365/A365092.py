# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365092

from functools import lru_cache
from sympy import factorint, isprime
@lru_cache(maxsize=None)
def A365092(n): return n-1<<1 if n <= 2 else (sum(A365092(p)+A365092(e) for p, e in factorint(n).items()) if not isprime(n) else A365092(n-1)+1) # _Chai Wah Wu_, Aug 23 2023

