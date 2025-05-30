# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368107

import heapq
from itertools import islice
from sympy import nextprime
def agen(): # generator of terms
    v, h, m, nextp = 4, [(4, 2)], 4, 3
    while True:
        v, p = heapq.heappop(h)
        yield v
        if v >= m:
            m = nextp**nextp
            heapq.heappush(h, (m, nextp))
            nextp = nextprime(nextp)
        heapq.heappush(h, (v*p**p, p))
print(list(islice(agen(), 31))) # _Michael S. Branicky_, Jan 16 2024

