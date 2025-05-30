# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A247152

from sympy import isprime, prime
def a(n):
    k, target = 4, str(prime(n))
    while not target in str(k) or isprime(k): k += 1
    return k
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Dec 30 2021

