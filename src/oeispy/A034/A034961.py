# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A034961

from sympy import nextprime
from itertools import count, islice
def agen(): # generator of terms
    p, q, r = 2, 3, 5
    while True:
        yield p + q + r
        p, q, r = q, r, nextprime(r)
print(list(islice(agen(), 54))) # _Michael S. Branicky_, Dec 27 2022

