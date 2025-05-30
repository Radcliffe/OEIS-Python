# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A050897

from sympy import isprime
def afind(limit, startat=0):
  pow2 = 2**startat
  for k in range(startat, limit+1):
    if isprime(277*pow2-1): print(k, end=", ")
    pow2 *= 2
afind(3333) # _Michael S. Branicky_, May 21 2021

