# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A078514

from sympy import factorint
def aupto(limit):
  alst = []
  for k in range(4, limit+1):
    f = factorint(k)
    if min(f) == max(f[p] for p in f): alst.append(k)
  return alst
print(aupto(338)) # _Michael S. Branicky_, Apr 12 2021

