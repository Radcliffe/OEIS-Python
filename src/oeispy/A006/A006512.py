# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A006512

from sympy import primerange, isprime
print([n for n in primerange(1, 2001) if isprime(n - 2)]) # _Indranil Ghosh_, Jul 20 2017

