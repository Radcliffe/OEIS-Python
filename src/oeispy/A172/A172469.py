# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A172469

from itertools import count, islice
from sympy import isprime
def A172469_gen(): # generator of terms
    yield from (7, 43)
    for n in count(50,50):
        for m in (1,7,43,49):
            if isprime(n+m):
                yield n+m
A172469_list = list(islice(A172469_gen(),48)) # _Chai Wah Wu_, Apr 28 2025

