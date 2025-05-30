# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339485

from functools import lru_cache
from sympy import sieve, isprime
@lru_cache(maxsize=None)
def b(n, s, c):
    if n == 0: return int(c and s%c == 0 and isprime(s//c))
    return b(n-1, s, c) + b(n-1, s+sieve[n], c+1)
a = lambda n: b(n, 0, 0)
print([a(n) for n in range(1, 41)]) # _Michael S. Branicky_, Oct 06 2022

