# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363680

from sympy import totient, integer_nthroot
def a(n):
  x = n
  c = 0
  while not integer_nthroot(x,3)[1]:
    x = totient(x)
    c += 1
  return c

