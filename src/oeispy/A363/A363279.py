# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363279

from collections import Counter
from itertools import count, islice
def agen(): # generator of terms
    yield from [1, 2]
    sumsn, c =  [2, 3], Counter([1, 2, 3])
    for n in count(2):
        an = c[n]
        yield an
        sumsn = [an] + [s + an for s in sumsn]
        c.update(sumsn)
print(list(islice(agen(), 86))) # _Michael S. Branicky_, May 25 2023

