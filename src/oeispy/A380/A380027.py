# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380027

from itertools import count, islice
from sympy import isprime, primepi, primorial
def A002110(n): return primorial(n) if n > 0 else 1
def agen(an=2): # generator of terms
    while True:
        yield an
        an = next(s for k in range(primepi(an)-1, -1, -1) if isprime(s:=an+A002110(k)))
print(list(islice(agen(), 6))) # _Michael S. Branicky_, Jan 11 2025

