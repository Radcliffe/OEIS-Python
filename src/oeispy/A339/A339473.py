# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339473

from math import isqrt
def ok(k): r = isqrt(k); return k % r != 0 and k**2 % r == 0
print(list(filter(ok, range(1, 1351)))) # _Michael S. Branicky_, Apr 24 2021

