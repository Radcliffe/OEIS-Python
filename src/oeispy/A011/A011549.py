# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A011549

from sympy import N, sqrt
def a(n): return int(N(sqrt(3), n+1)*10**n)
print([a(n) for n in range(20)]) # _Michael S. Branicky_, Jan 17 2021

