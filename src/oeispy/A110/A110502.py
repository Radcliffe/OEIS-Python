# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A110502

from math import isqrt
from itertools import groupby
def is_nt_sqr(n): # is nontrivial square
    return n > 1 and isqrt(n)**2 == n
def ok(n):
    b = bin(n)[2:]
    return any(k == '0' and is_nt_sqr(len(list(g))) for k, g in groupby(b))
print(list(filter(ok, range(532)))) # _Michael S. Branicky_, Sep 01 2021

