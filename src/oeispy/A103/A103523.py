# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A103523

from sympy import isprime, primerange as prange
def auptop(lim):
  return [int(str(p)+str(p+100)) for p in prange(2, lim+1) if isprime(p+100)]
print(auptop(577)) # _Michael S. Branicky_, Jul 04 2021

