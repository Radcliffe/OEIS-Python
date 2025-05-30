# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A077664

from math import gcd
def arow(n):
    rown, k = [], n + 1
    while len(rown) < n:
        if gcd(k, n) == 1: rown.append(k)
        k += 1
    return rown
def agen(rows):
    for n in range(1, rows+1): yield from arow(n)
print([an for an in agen(12)]) # _Michael S. Branicky_, Sep 21 2021

