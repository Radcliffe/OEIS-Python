# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062037

from math import prod
def ok(n): d = list(map(int, str(n))); return prod(d) == 6*sum(d)
print([k for k in range(1, 3000) if ok(k)]) # _Michael S. Branicky_, Aug 02 2022

