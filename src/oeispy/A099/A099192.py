# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A099192

from sympy import isprime
def aupto(limit):
  alst = []
  for k in range(1, limit+1):
    if isprime(10**12*k + 235711131719): alst.append(k)
  return alst
print(aupto(500)) # _Michael S. Branicky_, May 12 2021

