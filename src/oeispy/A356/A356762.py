# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356762

from sympy import isprime, nextprime
from itertools import count, islice
def agen(): # generator of terms
    p, q = 2, 3
    while True:
        if all(isprime(t) for t in [p*q+p+q, p*q-p-q, p*q+2*(p+q), p*q-2*(p+q)]):
            yield p
        p, q = q, nextprime(q)
print(list(islice(agen(), 15))) # _Michael S. Branicky_, Aug 26 2022

