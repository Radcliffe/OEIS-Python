# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A334527

from sympy import factorint
def sd(n): return sum(map(int, str(n)))
def ok(n):
  sdn = sd(n)
  if sdn == 0 or n%sdn != 0: return False # not Niven
  f = factorint(n)
  return sum(f[p] for p in f) > 1 and sdn == sum(sd(p)*f[p] for p in f)
print(list(filter(ok, range(9999)))) # _Michael S. Branicky_, Apr 27 2021

