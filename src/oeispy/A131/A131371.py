# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A131371

from sympy import factorint
from sympy.utilities.iterables import multiset_permutations as mp
def c(n):
    return sum(factorint(n).values()) == 2
def a(n):
    return sum(1 for p in mp(str(n)) if p[0]!="0" and c(t:=int("".join(p))))
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Jun 11 2023

