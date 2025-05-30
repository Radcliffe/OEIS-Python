# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A163981

from sympy import isprime, nextprime, prime
def a(n):
    pn = prime(n); pn1 = nextprime(pn); k = 1
    while not isprime(pn1*k - pn): k += 1
    return pn1*k - pn
print([a(n) for n in range(1, 62)]) # _Michael S. Branicky_, Jul 02 2021

