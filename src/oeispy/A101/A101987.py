# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A101987

from math import prod
from sympy import sieve
def A051801(n): return prod(int(d) for d in str(n) if d != '0')
def a(n): return A051801(sieve[n])
print([a(n) for n in range(1, 78)]) # _Michael S. Branicky_, Mar 11 2022

