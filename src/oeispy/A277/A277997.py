# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A277997

from sympy import isprime
from itertools import count, islice
def nextcomposite(n): return next(k for k in count(n+1) if not isprime(k))
def agen(): # generator of terms
    an, a, nextc = 1, {1}, 4
    while True:
        yield an
        c = nextc
        while c in a or not isprime(abs(c-an)) or abs(c-an) in a:
            c = nextcomposite(c)
        a.add(c)
        a.add(abs(c-an))
        an = c
        while nextc in a: nextc = nextcomposite(nextc)
print(list(islice(agen(), 74))) # _Michael S. Branicky_, Dec 23 2024

