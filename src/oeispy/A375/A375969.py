# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375969

from math import gcd
from itertools import count, islice
def agen():
    m = 0
    yield 0
    for w in count(1): # w = number of digits
        for s in range(1, 9*w+1): # s = sum of digits
            if gcd(s, w) == 1:
                d, r = [1] + [0 for _ in range(w-1)], s-1
                for k in range(w-1, -1, -1):
                    d[k], r = d[k] + min(r, 9), r - min(r, 9)
                yield int("".join(map(str, d)))
print(list(islice(agen(), 54)))
# _Michael S. Branicky_, Sep 08 2024 after _Rémy Sigrist_ PARI in link

