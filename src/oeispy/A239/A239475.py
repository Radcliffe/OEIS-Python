# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A239475

import sympy
from sympy import isprime
def TwoBoth(x):
  for k in range(1,10**7):
    if isprime(k**x+x) and isprime(k**x-x):
      return k
x = 1
while x < 100:
  if TwoBoth(x) != None:
    print(TwoBoth(x))
  else:
    print(0)
  x += 1

