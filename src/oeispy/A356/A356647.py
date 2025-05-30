# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356647

from itertools import count, islice
def agen(): # generator of terms
    for k in count(1):
        for j in range(1, k+1):
            yield from range(j, k+1)
print(list(islice(agen(), 87))) # _Michael S. Branicky_, Oct 11 2022

