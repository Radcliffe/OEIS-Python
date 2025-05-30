# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A240083

import sympy
from sympy import isprime
def Lep(n):
  for k in range(2*10**3):
    num = k**n
    for i in range(2, k):
      num -= i**n
      if num < 0:
        return None
    if isprime(num):
      return k
n = 1
while n < 10**3:
  if Lep(n) != None:
    print(n)
  n += 1

