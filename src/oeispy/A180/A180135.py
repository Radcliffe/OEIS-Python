# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180135

from sympy import isprime, nextprime, prevprime
def ok(n):
  if n <= 5: return n == 5
  return not isprime(n//2) and n == prevprime(n//2) + nextprime(n//2)
def a(n):
  k, pow11 = 1, 11**n
  while not ok(k*pow11): k += 1
  return k
print([a(n) for n in range(62)]) # _Michael S. Branicky_, May 18 2021

