# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365018

from itertools import islice
def agen(): # generator of terms
    an, bins, concats = 1, {"1"}, set()
    while True:
        yield an
        while (bn:=bin(an:=an+1)[2:]) in concats: pass
        concats |= {bn+bi for bi in bins} | {bi+bn for bi in bins}
        bins.add(bn)
print(list(islice(agen(),62))) # _Michael S. Branicky_, Sep 29 2023

