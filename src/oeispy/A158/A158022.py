# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A158022

from math import isqrt
a, k, l = [], 0, 0
while len(a) < 40:
    l += len(str(k))
    if l == isqrt(l) ** 2: a.append(k)
    k += 1
print(a) # _Dominic McCarty_, Mar 28 2025

