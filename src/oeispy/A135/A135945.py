# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A135945

from itertools import product
from sympy import isprime, primerange
def a(n):
    p2 = list(map(str, primerange(10, 100)))
    return sum(1 for p in product(p2, repeat=n) if isprime(int("".join(p))))
print([a(n) for n in range(1, 6)]) # _Michael S. Branicky_, Feb 13 2023

