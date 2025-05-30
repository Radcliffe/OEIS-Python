# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362986

from itertools import count, islice
from math import prod
from sympy import factorint
def A362986_gen(): # generator of terms
    for n in count(1):
        f = factorint(n)
        if all(e>2 for e in f.values()):
            yield prod((p**(e+1)-1)//(p-1) for p,e in f.items())
A362986_list = list(islice(A362986_gen(),20)) # _Chai Wah Wu_, May 21 2023

