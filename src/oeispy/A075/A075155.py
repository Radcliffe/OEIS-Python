# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A075155

from sympy import lucas
def a(n):  return lucas(n)**3
print([a(n) for n in range(25)]) # _Michael S. Branicky_, Aug 01 2021

