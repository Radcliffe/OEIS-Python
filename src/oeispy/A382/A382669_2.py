# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382669

from itertools import count, islice
from sympy import isprime
def A382669_gen(): # generator of terms
    yield 2
    yield from filter(lambda m: isprime(p:=m**2+1) and isprime(p+(m**4>>1)),(10*k for k in count(1)))
A382669_list = list(islice(A382669_gen(),45)) # _Chai Wah Wu_, May 02 2025

