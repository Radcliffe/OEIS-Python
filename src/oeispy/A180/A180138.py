# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180138

from sympy import isprime, nextprime, prevprime
def sum2succ(n):
  if n <= 5: return n == 5
  return not isprime(n//2) and n == prevprime(n//2) + nextprime(n//2)
def T(b, e):
  k, powb = 1, b**e
  while not sum2succ(k*powb): k += 1
  return k
def atodiag(maxd): # maxd antidiagonals
  return [T(b-e, e) for b in range(2, maxd+2) for e in range(b-1)]
print(atodiag(13)) # _Michael S. Branicky_, May 05 2021

