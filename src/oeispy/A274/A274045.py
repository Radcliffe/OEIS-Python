# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A274045

from sympy import isprime,nextprime
for i in range(3,1500001,2):
  if isprime(i) and nextprime(i) == i+72: print(i,end=', ')

