# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000026

from math import prod
from sympy import factorint
def a(n): f = factorint(n); return prod(p*f[p] for p in f)
print([a(n) for n in range(1, 73)]) # _Michael S. Branicky_, May 27 2021

