# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A111233

from fractions import Fraction
from functools import lru_cache
@lru_cache(maxsize=None)
def b(n, soh, c):
    if n == 0: return int(soh.denominator == 1)
    return b(n-1, soh, c) + b(n-1, soh+Fraction(1, n), c+1)
a = lambda n: b(n, 0, 0) - 1 # subtract empty set
print([a(n) for n in range(1, 21)]) # _Michael S. Branicky_, Aug 11 2022

