# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354182

from itertools import count, islice
def agen(): # generator of terms
    aset, k, mink = set(), 0, 1
    for n in count(1):
        aset.add(k); yield k; k = mink
        while k in aset or n&(n+k): k += 1
        while mink in aset: mink += 1
print(list(islice(agen(), 68))) # _Michael S. Branicky_, May 18 2022

