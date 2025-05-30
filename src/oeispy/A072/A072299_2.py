# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A072299

# uses ok, import above
from itertools import count, islice
def agen(): # generator of terms
    for e in count(1):
        for f in [1, 2, 3, 5, 7, 9]:
            base = f*10**(e-1)
            if f in {2, 5}: yield base; continue
            for k in range(base, base+10**(e-1)):
                if ok(k): yield k
print(list(islice(agen(), 50))) # _Michael S. Branicky_, Sep 23 2024

