# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367354

from itertools import islice
def agen(start=10): # generator of terms
    an, y = start, 1
    while y < 10:
        yield an
        an, y = an + 10*(an%10), 1
        while y < 10:
            if str(an+y)[0] == str(y):
                an += y
                break
            y += 1
print(list(islice(agen(), 50))) # _Michael S. Branicky_, Nov 18 2023

