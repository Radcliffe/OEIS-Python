# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A069710

from itertools import count, islice
from collections import Counter
from sympy.utilities.iterables import partitions, multiset_permutations
from sympy import isprime
def A069710_gen(): # generator of terms
    for l in count(1):
        for i in range(1,min(9,l)+1):
            yield from sorted(q for q in (int(str(i)+''.join(map(str,j))) for s,p in partitions(l-i,k=9,size=True) for j in multiset_permutations([0]*(l-1-s)+list(Counter(p).elements()))) if isprime(q))
A069710_list = list(islice(A069710_gen(),30)) # _Chai Wah Wu_, Nov 28 2023

