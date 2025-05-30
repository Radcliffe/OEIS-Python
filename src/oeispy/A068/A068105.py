# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068105

from sympy import isprime
def a(n):
  if n < 2: return list([2, 5])[n]
  n5s, i, pow10 = int('5'*n), 1, 1
  while True:
    i = 1
    while i < pow10:
      t = n5s * pow10 + i
      if isprime(t): return t
      i += 2
    pow10 *= 10
print([a(n) for n in range(20)]) # _Michael S. Branicky_, Feb 05 2021

