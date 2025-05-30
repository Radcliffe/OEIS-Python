# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A229970

from sympy import divisors
def PD(n):
  p = 1
  for i in divisors(n):
    if i != n:
      p *= i
  return p
def pal(n):
  r = ''
  for i in str(n):
    r = i + r
  return r == str(n)
{print(n, end=', ') for n in range(1, 10**4) if pal(PD(n)) and (PD(n)-1) and PD(n)-n}
## Simplified by _Derek Orr_, Apr 05 2015

