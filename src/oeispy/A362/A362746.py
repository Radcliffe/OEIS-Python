# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362746

from itertools import islice
from collections import Counter
def agen(): # generator of terms
    aprev, an, anext, c = 0, 1, 1, Counter({(1, 1)})
    while True:
        aprev, an, anext = an, anext, c[an, anext]
        c[an, anext] += 1
        if aprev != anext: c[anext, an] +=  1
        yield an
print(list(islice(agen(), 100))) # _Michael S. Branicky_, May 02 2023

