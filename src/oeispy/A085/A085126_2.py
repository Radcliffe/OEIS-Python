# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A085126

# faster for initial segment of sequence
import heapq
from itertools import islice
def A085126gen(): # generator of terms
    v, oldv, h, psmooth_primes, = 1, 0, [1], [2, 3, 5, 7]
    while True:
        v = heapq.heappop(h)
        if v != oldv:
            yield 3*v
            oldv = v
            for p in psmooth_primes:
                    heapq.heappush(h, v*p)
print(list(islice(A085126gen(), 65))) # _Michael S. Branicky_, Sep 17 2024

