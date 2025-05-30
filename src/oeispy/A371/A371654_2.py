# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371654

from itertools import count, islice, combinations_with_replacement
from sympy import isprime
from sympy.utilities.iterables import multiset_permutations
def A371654_gen(): # generator of terms
    for l in count(1):
        xlist = []
        for p in combinations_with_replacement('0123456789',l):
            if isprime(int(''.join(p))):
                xlist.extend(int(''.join(d)) for d in multiset_permutations(p) if d[0] != '0' and d[-1] != '0')
        yield from sorted(xlist)
A371654_list = list(islice(A371654_gen(),20)) # _Chai Wah Wu_, Apr 10 2024

