# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355069

from sympy import prime
def f(n):
  S = 0
  n2n=(n*n) - n
  for x in range(1, n2n + 1):
    for y in range(x + 1 , n2n + 1):
      if ((pow(x, y, n) == pow(y, x, n))):
        S += 2
  return S + n2n
def a(n): return f(prime(n))

