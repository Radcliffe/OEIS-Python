# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A086151

from sympy import isprime
from sympy.utilities.iterables import multiset_permutations as mp
def a(n): return sum(1 for p in mp(str(2**n)) if isprime(int("".join(p))))
print([a(n) for n in range(1, 31)]) # _Michael S. Branicky_, May 25 2023

