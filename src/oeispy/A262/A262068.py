# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A262068

# MS() in A262278
from numba import njit
@njit()  # comment out for n >= 32
def a(n):
  if n == 0: return 1  # by convention
  s = 0
  for b in range(int(2**(2*n-1))):
    s += MS(b, n) >= 1
  return 2*s
print([a(n) for n in range(10)]) # _Michael S. Branicky_, Dec 29 2020

