# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A160530

from itertools import groupby
def ok(n): return all(len(list(g))%2 == 1 for k, g in groupby(bin(n)[2:]))
print([i for i in range(1, 280) if ok(i)]) # _Michael S. Branicky_, Jan 04 2021

