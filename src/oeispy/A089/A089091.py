# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A089091

from math import gcd
def a(n):
    k, m = 3, n*(n+1)
    while gcd(k, m) != 1: k += 2
    return k*k
print([a(n) for n in range(1, 79)]) # _Michael S. Branicky_, Sep 25 2021

