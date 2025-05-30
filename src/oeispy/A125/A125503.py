# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A125503

from sympy import isprime
from fractions import Fraction
def a(n):
    Hkn, k = Fraction(1, 1), 1
    while not isprime(Hkn.numerator):
        k += 1
        Hkn += Fraction(1, k**n)
    return k
print([a(n) for n in range(1, 20)]) # _Michael S. Branicky_, Jun 11 2022

