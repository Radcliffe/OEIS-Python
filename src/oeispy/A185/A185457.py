# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A185457

from sympy import im, I
def a(n): return abs(im((2 + I)**(2**n)))
print([a(n) for n in range(11)]) # _Indranil Ghosh_, Jul 08 2017

