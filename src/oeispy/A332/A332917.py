# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A332917

from fractions import Fraction
def f(n): return Fraction(40+6*n-4*n**2, 2**n) - Fraction(83, 2) + Fraction(331*n, 12) - 6*n**2 + Fraction(2*n**3, 3)
def a(n): return (f(n).denominator).bit_length() - 1
print([a(n) for n in range(3, 71)]) # _Michael S. Branicky_, Aug 31 2021

