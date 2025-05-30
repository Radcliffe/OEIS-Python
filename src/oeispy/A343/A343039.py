# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343039

from math import isqrt
def aupton(terms):
  alst = [1]
  for n in range(2, terms+1):
    alst.append((isqrt(alst[-1] + n)+1)**2 - alst[-1] - n)
  return alst
print(aupton(79)) # _Michael S. Branicky_, Apr 03 2021

