# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350778

from fractions import Fraction
from sympy import prime, primerange
def aupton(N, m=3): # m is safety factor
    f = (Fraction(i, p) for i, p in enumerate(primerange(2, prime(m*N)), 1))
    return [fn.numerator for fn in sorted(f, reverse=True)][:N]
print(aupton(100)) # _Michael S. Branicky_, Jan 15 2022

