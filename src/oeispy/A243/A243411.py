# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A243411

import sympy
from sympy import isprime
from sympy import prime
def a(n):
  for k in range(1,10**8):
    if isprime(prime(k)*10**n-1) and isprime(prime(k)*10**n-3) and isprime(prime(k)*10**n-7) and isprime(prime(k)*10**n-9):
      return prime(k)
n = 1
while n < 100:
  print(a(n),end=', ')
  n+=1

