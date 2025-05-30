# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346154

from sympy import isprime
def a(n):
    if n > 1 and n%3 == 1: return 0
    k = 2
    while not isprime(n**k + n + 1): k += 1
    return n**k + n + 1
print([a(n) for n in range(1, 52)]) # _Michael S. Branicky_, Jul 07 2021

