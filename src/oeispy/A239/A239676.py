# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A239676

import sympy
from sympy import isprime
def Pow3(n):
  for k in range(10**4):
    if isprime(k*(3**n)+1):
      return n
n = 1
while n < 100:
  print(Pow3(n))
  n += 1

