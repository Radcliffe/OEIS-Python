# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A122280

from math import gcd
from sympy import isprime
from itertools import islice
def agen(): # generator of terms
    aset, an, mink = {1, 2}, 2, 3
    yield from sorted(aset)
    while True:
        k = mink
        while k in aset or not isprime(gcd(an, k)): k += 1
        an = k; aset.add(an); yield an
        while mink in aset: mink += 1
print(list(islice(agen(), 72))) # _Michael S. Branicky_, Oct 13 2022

