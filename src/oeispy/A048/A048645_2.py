# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A048645

from itertools import count, islice
def agen(): # generator of terms
    for d in count(0):
        msb = 2**d
        yield msb
        for lsb in range(d):
            yield msb + 2**lsb
print(list(islice(agen(), 60))) # _Michael S. Branicky_, Jan 22 2022

