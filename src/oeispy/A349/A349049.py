# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349049

from sympy import harmonic, factorint
def a(n): return sum(factorint(harmonic(n).denominator).values())
print([a(n) for n in range(1, 78)]) # _Michael S. Branicky_, Nov 07 2021

