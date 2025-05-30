# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A292349

from sympy import isprime, primerange
for i in primerange(1, 1000):
  delta = 0
  bit = 1
  while  bit <= i:
    if isprime(i^bit): delta += 1
    else:              delta -= 1
    bit*=2
  if delta > 0:  print(str(i), end=',')

