# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055143

from itertools import count, islice
def agen():
    k, chap = 1, "1"
    for n in count(1):
        while len(chap) < n: k += 1; chap += bin(k)[2:]
        yield int(chap[:n], 2)
print(list(islice(agen(), 34))) # _Michael S. Branicky_, Oct 06 2022

