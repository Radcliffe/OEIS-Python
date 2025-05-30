# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377370

from sympy import isprime
from itertools import count
def a(n):
    ending = int(("01"*n)[-n:])
    if n&1 and isprime(ending): return ending
    return next(i for i in count(10**n+ending, 10**n) if isprime(i))
print([a(n) for n in range(1, 21)]) # _Michael S. Branicky_, Jan 26 2025

