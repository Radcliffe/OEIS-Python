# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A173688

from itertools import count, islice, combinations_with_replacement
from math import factorial
from sympy import isprime
from sympy.utilities.iterables import multiset_permutations
def A173688_gen(): # generator of terms
    for l in count(0):
        for i in range(1,10):
            fi = factorial(i)**2
            yield from sorted(int(str(i)+''.join(map(str,k))) for j in combinations_with_replacement(range(10), l) for k in multiset_permutations(j) if isprime(fi+sum(map(lambda n:factorial(n)**2,j))))
A173688_list = list(islice(A173688_gen(),50)) # _Chai Wah Wu_, Feb 23 2023

