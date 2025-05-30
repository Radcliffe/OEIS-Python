# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A121229

from itertools import islice
def agen(): # generator of terms
    disallowed, prevk, k = {1, 2}, 2, 3; yield from [1, 2]
    while True:
        while k in disallowed: k += 1
        yield k; disallowed.update([k, k*prevk]); prevk = k
print(list(islice(agen(), 72))) # _Michael S. Branicky_, Sep 23 2022

