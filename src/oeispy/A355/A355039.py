# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355039

from itertools import islice
from sympy import factorint, isprime, nextprime
def A355039_gen(): # generator of terms
    p, q = 3, 5
    while True:
        yield from (n for n in range(p+2,q,2) if max((f:=factorint(n)).values()) == 1 and not any((n-1) % (p-1) for p in f) and isprime(len(f)))
        p, q = q, nextprime(q)
A355039_list = list(islice(A355039_gen(),20)) # _Chai Wah Wu_, Jun 16 2022

