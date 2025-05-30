# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A169902

from math import gcd
for n in range(1, 1001):
  a_n = 1
  res = []
  for addend in range(1, n//2+1): res.append(addend*(n - addend))
  for dividend in range(1, n+1):
    if not n%dividend: res.append(dividend + n//dividend)
    if dividend*dividend >= n: break
  for i in res: a_n *= i // gcd(a_n, i)
  print(n, a_n)
# _Charlie Neder_, Oct 09 2018

