# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A088253

from gmpy2 import is_prime
from itertools import count
def a(n): return next(t for t in (int("".join(str(i) for i in range(k, k+n*n, n))) for k in count(1)) if is_prime(t)) if n%3 else 0
print([a(n) for n in range(1, 19)]) # _Michael S. Branicky_, Jun 23 2023

