# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A113646

from sympy import isprime
def a(n):
  an = max(4, n)
  while isprime(an): an += 1
  return an
print([a(n) for n in range(1, 73)]) # _Michael S. Branicky_, Apr 04 2021

