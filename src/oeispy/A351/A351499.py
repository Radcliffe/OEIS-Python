# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351499

from math import gcd
from itertools import islice
def agen(): # generator of terms
    an, aset, mink, seen = 1, {1}, 2, {1}
    yield 1
    while True:
        if mink%2 and mink not in seen: yield mink; seen.add(mink)
        k = mink
        while k in aset or gcd(an, k) != 1 or k-an == 1: k += 1
        an = k; aset.add(an)
        while mink in aset: mink += 1
print(list(islice(agen(), 42))) # _Michael S. Branicky_, May 03 2022

