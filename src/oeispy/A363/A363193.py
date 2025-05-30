# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363193

from bisect import bisect
from itertools import count, islice
def agen(): # generator of terms
    an, a, locs = 1, [None, 1], {1: [1]}
    yield 1
    for n in count(2):
        k = n-an
        an = bisect(locs[a[k]], k) # sum(1 for i in locs[a[k]] if i <= k)
        a.append(an)
        if an not in locs: locs[an] = []
        locs[an].append(n)
        yield an
print(list(islice(agen(), 86))) # _Michael S. Branicky_, May 23 2023

