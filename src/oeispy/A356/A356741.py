# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356741

from sympy import isprime, nextprime, prime
def a(n):
    pn, pm, pmsharp = prime(n), 2, 2
    while not isprime(pn + pmsharp): pm = nextprime(pm); pmsharp *= pm
    return pm
print([a(n) for n in range(2, 89)]) # _Michael S. Branicky_, Sep 04 2022

