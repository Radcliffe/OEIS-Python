# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A237641

import sympy
from sympy import isprime
def poly2(x):
  if isprime(x):
    f = x**2-x-1
    if isprime(f**2-f-1):
      return True
  return False
x = 1
while x < 10**5:
  if poly2(x):
    if isprime(x**2-x-1):
      print(x**2-x-1)
  x += 1

