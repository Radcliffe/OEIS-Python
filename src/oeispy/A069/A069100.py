# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A069100

from sympy import nextprime
def a(n):  return nextprime(10**(n-1), ith=n)
print([a(n) for n in range(1, 21)]) # _Michael S. Branicky_, Jun 16 2021

