# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381019

# see link for faster version
from math import gcd
from itertools import count, islice
def agen(): # generator of terms
    alst, aset, an, m = [1], {1}, 1, 2
    for n in count(2):
        yield an
        an = next(k for k in count(m) if k not in aset and all(gcd(alst[-j], k) == 1 for j in range(1, min(k, n-1)+1)))
        alst.append(an)
        aset.add(an)
        while m in aset: m += 1
print(list(islice(agen(), 61))) # _Michael S. Branicky_, Feb 13 2025

