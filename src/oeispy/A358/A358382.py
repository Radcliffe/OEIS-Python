# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358382

from itertools import islice
from sympy import isprime, nextprime
def agen():
    p, q, r = 2, 3, 5
    while True:
        rpq, pq = r*(p+q), p*q
        if all(isprime(t) for t in [rpq+pq, rpq-pq]): yield p
        p, q, r = q, r, nextprime(r)
print(list(islice(agen(), 48))) # _Michael S. Branicky_, Nov 20 2022

