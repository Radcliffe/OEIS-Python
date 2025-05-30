# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A164834

from sympy import isprime
def aupto(limit):
  i, c, alst = 1, 1, []
  while c <= limit + 1:
    if isprime(c-2) and c-1 <= limit: alst.append(c-1)
    if isprime(c+2) and c+1 <= limit: alst.append(c+1)
    i += 1
    c = i**3
  return alst
print(aupto(5000212)) # _Michael S. Branicky_, Feb 28 2021

