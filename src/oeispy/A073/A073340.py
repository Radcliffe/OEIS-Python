# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A073340

from sympy import isprime
def afind(limit):
  i, fnm2, fnm1 = 1, 1, 1
  while i < limit:
    if isprime(fnm2) and isprime(fnm2 + fnm1):
      print(i, i+2, sep=", ", end=", ")
    i, fnm2, fnm1 = i+1, fnm1, fnm2 + fnm1
afind(600) # _Michael S. Branicky_, Mar 05 2021

