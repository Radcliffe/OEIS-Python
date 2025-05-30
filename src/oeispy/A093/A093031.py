# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A093031

from itertools import islice
from collections import Counter
def agen(): # generator of terms
    an, c = 0, Counter()
    while True:
        yield an
        c.update(list(str(an)))
        m, argm = float('inf'), None
        for d in "1234567890":
            if c[d] < m:
                m, argm = c[d], d
        an += 10 if argm == "0" else int(argm)
print(list(islice(agen(), 60))) # _Michael S. Branicky_, Oct 01 2024

