# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371260

from itertools import count, islice
def agen(): # generator of terms
    h1, h2, h3 = 1, 2, 3
    while True:
        if h3 - h2 == h2 - h1: yield h1
        h1, h2, h3 = h2, h3, next(k for k in count(h3+1) if k%sum(map(int, str(k))) == 0)
print(list(islice(agen(), 52))) # _Michael S. Branicky_, Mar 16 2024

