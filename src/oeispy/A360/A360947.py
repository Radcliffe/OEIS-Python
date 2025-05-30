# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360947

from itertools import count, islice
def agen(): # generator of terms
    an, aset, mink = 1, set(), 2
    while True:
        yield an; aset.add(an); t = str(an)[::-1]; mink = max(int(t)-an, 2)
        an = next(k for k in count(mink) if k not in aset and t in str(an+k))
print(list(islice(agen(), 51))) # _Michael S. Branicky_, Oct 15 2023

