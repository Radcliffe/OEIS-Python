# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A084832

from sympy import isprime
def afind(limit):
  n, twoRn = 1, 2
  for n in range(1, limit+1):
    if isprime(twoRn-1): print(n, end=", ")
    twoRn = 10*twoRn + 2
afind(700) # _Michael S. Branicky_, Apr 18 2021

