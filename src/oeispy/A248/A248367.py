# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A248367

from sympy import isprime
for n in range(1,10000001,2):
  if isprime(n) and isprime(n+2) and isprime(n+36) and isprime(n+38): print(n,end=', ')

