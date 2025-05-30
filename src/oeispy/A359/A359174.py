# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359174

from sympy import nextprime
from itertools import count, islice
def agen(): # generator of terms
    p, q, r = 2, 3, 5
    while True:
        t = int(str(p+q+r)[::-1])
        if any(t%s == 0 for s in (p, q, r)): yield p
        p, q, r = q, r, nextprime(r)
print(list(islice(agen(), 19))) # _Michael S. Branicky_, Dec 27 2022

