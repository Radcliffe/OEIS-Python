# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347338

from sympy import divisor_count
from functools import lru_cache
@lru_cache(maxsize=None)
def tau(n): return divisor_count(n)
def a(n):
    k = 2
    while True:
        while tau(k) != tau(k+n): k += 1
        if not any(tau(m) == tau(k) for m in range(k+1, k+n)): return k
        k += 1
print([a(n) for n in range(1, 56)]) # _Michael S. Branicky_, Aug 27 2021

