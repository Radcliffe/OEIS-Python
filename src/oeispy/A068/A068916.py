# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068916

from sympy import factorint
def a(n):
  k = 1
  while True:
    f = factorint(k)
    if k == sum(f[d]*d**n for d in f): return k
    k += 1
for n in range(1, 8):
  print(a(n), end=", ") # _Michael S. Branicky_, Feb 16 2021

