# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A036343

import heapq
from sympy import isprime
from itertools import islice
def A036343_gen(): # generator of terms
    h = [(i, i) for i in range(1, 13)]
    while True:
        v, last = heapq.heappop(h)
        if isprime(v):
            yield v
        nxt = 12 if last == 1 else last-1
        shift = 10 if nxt < 10 else 100
        heapq.heappush(h, (v*shift+nxt, nxt))
print(list(islice(A036343_gen(), 16))) # _Michael S. Branicky_, May 20 2024

