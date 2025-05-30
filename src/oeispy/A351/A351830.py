# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351830

from math import isqrt
def a(n):
    t = n*(n+1)*(2*n+1)//6
    r = isqrt(t)
    return min(t - r**2, (r+1)**2 - t)
print([a(n) for n in range(66)]) # _Michael S. Branicky_, Feb 21 2022

