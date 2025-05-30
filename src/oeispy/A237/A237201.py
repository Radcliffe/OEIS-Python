# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A237201

import sympy
from sympy import isprime
from sympy import factorint
def PrimeFact(x):
  n = 9930000
  lst = []
  while n < 10**10:
    if not isprime(n):
      count = 0
      for i in range(n, n+x):
        if sum(factorint(i).values()) == x:
          count += 1
        else:
          n += 1
          break
      if count == x:
        return n
    else:
      n += 1

