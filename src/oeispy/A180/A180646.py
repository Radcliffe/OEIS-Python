# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180646

from sympy import isprime, totient
print([n for n in range(1, 1001) if isprime(3 + totient(n)**3)]) # _Indranil Ghosh_, Apr 02 2017

