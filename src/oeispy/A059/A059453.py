# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059453

from itertools import count, islice
from sympy import isprime, prime
def A059453_gen(): # generator of terms
    return filter(lambda p:not isprime(p>>1) and isprime(p<<1|1),(prime(i) for i in count(1)))
A059453_list = list(islice(A059453_gen(),10)) # _Chai Wah Wu_, Jul 12 2022

