# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356858

from math import prod
def a(n): return prod((5*k-1)//4 for k in range(1, n+1))
print([a(n) for n in range(23)]) # _Michael S. Branicky_, Sep 01 2022

