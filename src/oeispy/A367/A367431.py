# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367431

from sympy import prime
from itertools import count, islice
def a(n):
    return int("".join(map(str, range(1 if n<2 else prime(n-1)+1, prime(n)+1))))
print([a(n) for n in range(1, 31)]) # _Michael S. Branicky_, Nov 18 2023

