# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A157902

from num2words import num2words
from itertools import count, islice
def c(n): return sum(1 for c in num2words(n) if c in "bcdfghjklmnpqrstvwxz")
def agen():
    n, adict = 1, dict()
    for k in count(1):
        v = c(k)
        if v == n: yield k; n += 1
print(list(islice(agen(), 39))) # _Michael S. Branicky_, Aug 09 2022

