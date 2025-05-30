# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380745

from collections import Counter
from itertools import count, islice
def agen(): # generator of terms
    an, digsetcount = 0, Counter()
    while True:
        yield an
        key = "".join(sorted(str(an)))
        an = digsetcount[key]
        digsetcount[key] += 1
print(list(islice(agen(), 82))) # _Michael S. Branicky_, Mar 24 2025

