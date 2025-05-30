# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A124936

from sympy import factorint
from itertools import count, islice
def agen(): # generator of terms
    yield 5
    nxt = 0
    for k in count(6, 2):
        prv, nxt = nxt, sum(factorint(k+1).values())
        if prv == nxt == 2: yield k
print(list(islice(agen(), 53))) # _Michael S. Branicky_, Nov 26 2022

