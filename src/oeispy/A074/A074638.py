# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A074638

from fractions import Fraction
def a(n): return sum(Fraction(1, 4*i-1) for i in range(1, n+1)).denominator
print([a(n) for n in range(1, 21)]) # _Michael S. Branicky_, Mar 21 2021

