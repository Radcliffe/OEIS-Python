# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342950

# faster for initial segment of sequence
import heapq
from itertools import islice
def A342950gen(): # generator of terms
    v, oldv, h, psmooth_primes, = 1, 0, [1], [2, 3, 5, 7]
    while True:
        v = heapq.heappop(h)
        if v != oldv:
            yield v
            oldv = v
            for p in psmooth_primes:
                if not (p==2 and v%5==0) and not (p==5 and v&1==0):
                    heapq.heappush(h, v*p)
print(list(islice(A342950gen(), 65))) # _Michael S. Branicky_, Sep 17 2024

