# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365628

from sympy import binomial, primorial
a = lambda n: binomial(primorial(n), n)
print([a(n) for n in range(1,10)])

