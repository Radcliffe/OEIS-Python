# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A107411

from itertools import islice
def agen(an=0):
    while True:
        yield an
        target, k = set(str(an)), an + 1
        while not (target <= set(str(k))): k += 1
        an = k
print(list(islice(agen(), 41))) # _Michael S. Branicky_, Nov 21 2022

