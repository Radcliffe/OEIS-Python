# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366487

from itertools import islice
def agen(): # generator of terms
    an, y = 1, 1
    while y < 10:
        prevan = an
        an, y = an + 10*(an%10), 1
        while y < 10:
            if str(an+y)[0] == str(y):
                an += y
                break
            y += 1
        yield an - prevan
print(list(islice(agen(), 99))) # _Michael S. Branicky_, Nov 12 2023

