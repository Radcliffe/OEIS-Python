# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A073946

from sympy import primepi, isprime
N = (x**2 for x in range(1, 1001))
print([n for n in N if isprime(n + primepi(n))]) # _Indranil Ghosh_, Mar 21 2017

