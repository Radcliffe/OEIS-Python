# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046346

from sympy import factorint
def ok(n):
  f = factorint(n)
  return sum(f[p] for p in f) > 1 and n % sum(p*f[p] for p in f) == 0
print(list(filter(ok, range(1250)))) # _Michael S. Branicky_, Apr 16 2021

