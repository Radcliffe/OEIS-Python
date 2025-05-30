# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A167764

from sympy import nextprime, prime
def a(n):
    pn1 = prime(n+1)
    k, pk, s = 1, 2, "2"
    while int(s)%pn1:
        k += 1; pk = nextprime(pk); s += str(pk)
    return k
print([a(n) for n in range(1, 65)]) # _Michael S. Branicky_, Oct 03 2021

