# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355034

from sympy import isprime
from sympy.ntheory.digits import digits
def a(n):
    b = 2
    while not isprime(sum(digits(n, b)[1:])): b += 1
    return b
print([a(n) for n in range(2, 89)]) # _Michael S. Branicky_, Jun 16 2022

