# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352912

from sympy import isprime, prime
from itertools import count, islice
def agen(): # generator of terms
    for n in count(1):
        pn, fk = prime(n), 1
        for k in range(1, pn+1):
            if isprime(pn + fk): yield pn + fk
            fk *= k
print(list(islice(agen(), 51))) # _Michael S. Branicky_, Apr 16 2022

