# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A175930

from itertools import groupby
def a(n):
    c = "".join(bin(len(list(g)))[2:] for k, g in groupby(bin(n)[2:]))
    return int(c, 2)
print([a(n) for n in range(1, 75)]) # _Michael S. Branicky_, Oct 02 2021

