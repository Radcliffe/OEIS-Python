# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349848

from sympy import prime, primerange
def a(n): pn = prime(n); return sum(pn**pk for pk in primerange(1, pn+1))
print([a(n) for n in range(1, 12)]) # _Michael S. Branicky_, Dec 02 2021

