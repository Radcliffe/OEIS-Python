# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347042

from sympy import divisors, primeomega
def a(n):
    bigomegan = primeomega(n)
    return sum(bigomegan%primeomega(d) == 0 for d in divisors(n)[1:])
print([a(n) for n in range(1, 88)]) # _Michael S. Branicky_, Aug 18 2021

