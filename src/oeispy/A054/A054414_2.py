# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A054414

# faster for initial segment of sequence
from itertools import islice
def agen(): # generator of terms, after _Ruud H.G. van Tol_
    a, b, r = 2, 3, 1
    while True:
        yield r
        a <<= 2; b *= 3; r += 2
        if a > b: a <<= 1; b *= 3; r += 1
print(list(islice(agen(), 100))) # _Michael S. Branicky_, Oct 10 2024

