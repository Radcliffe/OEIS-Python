# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A165413

from itertools import groupby
def a(n): return len(set([len(list(g)) for k, g in groupby(bin(n)[2:])]))
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Jan 04 2021

