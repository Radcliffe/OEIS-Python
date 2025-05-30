# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046890

from sympy import isprime
from sympy.utilities.iterables import multiset_permutations as mp
from itertools import count, islice, combinations_with_replacement as mc
def nd(d): yield from ("".join((f,)+m) for f in "123456789" for m in mc("0123456789", d-1))
def c(s): return sum(1 for p in mp(s) if p[0]!="0" and isprime(int("".join(p))))
def agen(): # generator of sequence terms
    n, adict = 0, dict()
    for digs in count(1):
        for s in nd(digs):
            v = c(s)
            if v not in adict: adict[v] = int(s)
            while n in adict: yield adict[n]; n += 1
print(list(islice(agen(), 40))) # _Michael S. Branicky_, Feb 08 2023

