# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A324371

from math import prod
from sympy.ntheory import digits
from sympy import primefactors as pf
def a(n): return prod(p for p in pf(n) if sum(digits(n, p)[1:]) < p)
print([a(n) for n in range(1, 85)]) # _Michael S. Branicky_, Jul 03 2022

