# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A196421

from sympy import prime
def a(n): return prime(n) * n*(n+1)//2
print([a(n) for n in range(1, 41)]) # _Michael S. Branicky_, Sep 01 2022

