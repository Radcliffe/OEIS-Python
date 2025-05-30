# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353295

from math import isqrt
def a(n):
    s = n*(n+1)*(2*n+1)//6
    r = isqrt(s)
    d1, d2 = s-r**2, (r+1)**2-s
    return r**2 if d1 <= d2 else (r+1)**2
print([a(n) for n in range(45)]) # _Michael S. Branicky_, Jun 05 2022

