# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A037153

from sympy import factorial, nextprime
def a(n): fn = factorial(n); return nextprime(fn+1) - fn
print([a(n) for n in range(1, 66)]) # _Michael S. Branicky_, May 22 2022

