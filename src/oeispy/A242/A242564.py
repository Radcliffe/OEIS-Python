# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A242564

import sympy
from sympy import isprime
from sympy import prime
def Pr(n):
  for p in range(1,10**7):
    if isprime(prime(p)*(10**n)+1) and isprime(prime(p)*(10**n)+3) and isprime(prime(p)*(10**n)+7) and isprime(prime(p)*(10**n)+9):
      return prime(p)
n = 1
while n < 50:
  print(Pr(n))
  n += 1

