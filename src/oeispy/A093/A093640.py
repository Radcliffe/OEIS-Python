# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A093640

from sympy import divisors
def a(n):
    s = bin(n)[2:]
    return sum(1 for d in divisors(n, generator=True) if bin(d)[2:] in s)
print([a(n) for n in range(1, 102)]) # _Michael S. Branicky_, Jul 11 2022

