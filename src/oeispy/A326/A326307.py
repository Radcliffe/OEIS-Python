# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A326307

from collections import Counter
from itertools import count, islice
def agen(): # generator of terms
    digmultisetcount = Counter()
    for n in count(0):
        key = "".join(sorted(str(n)))
        digmultisetcount[key] += 1
        yield digmultisetcount[key]
print(list(islice(agen(), 88))) # _Michael S. Branicky_, Jan 30 2025

