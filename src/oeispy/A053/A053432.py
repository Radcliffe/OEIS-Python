# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A053432

from itertools import count, islice, combinations_with_replacement as cwr
def agen(): # generator of terms
    for d in count(1):
        out = sorted(int("".join(t)) for t in cwr("8549176320", d))
        yield from out[1-int(d==1):] # remove extra 0's
print(list(islice(agen(), 65))) # _Michael S. Branicky_, Aug 17 2022

