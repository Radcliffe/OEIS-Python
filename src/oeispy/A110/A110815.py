# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A110815

from math import isqrt
def a(n):
  m = isqrt(int('2'+'0'*(2*n-2)))
  while set(str(m*m)) & set(str(m)) != set(): m += 1
  return m
print([a(n) for n in range(1, 12)]) # _Michael S. Branicky_, Feb 17 2021

