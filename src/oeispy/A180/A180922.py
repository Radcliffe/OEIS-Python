# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180922

from sympy import factorint
def triprimes(n): f = factorint(n); return sum(f[p] for p in f) == 3
def a(n):
  an = max(1, 10**(n-1))
  while not triprimes(an): an += 1
  return an
print([a(n) for n in range(1, 21)]) # _Michael S. Branicky_, Apr 10 2021

