# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A101300

from sympy import nextprime
def a(n): return nextprime(nextprime(n))
print([a(n) for n in range(71)]) # _Michael S. Branicky_, Mar 03 2021

