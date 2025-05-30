# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A100380

from itertools import count, islice
from sympy import isprime, prime, primorial
def A002110(n): return primorial(n) if n > 0 else 1
def A100380(n):
    pn = prime(n)
    return next(k for k in count(0) if isprime(pn+A002110(k)))
print([a(n) for n in range(1, 101)]) # _Michael S. Branicky_, Jan 10 2025

