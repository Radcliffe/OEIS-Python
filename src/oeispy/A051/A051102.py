# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A051102

from sympy import floor, E, prime
def a(n):  return floor(E**prime(n))
print([a(n) for n in range(1, 19)]) # _Michael S. Branicky_, Jul 20 2021

