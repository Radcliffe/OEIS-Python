# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358127

from math import gcd
from itertools import count, islice
from sympy import prime
def A358127_gen(): # generator of terms
    a, b = [3], set()
    for n in count(2):
        q = prime(n)+1
        b |= set(gcd(p,q) for p in a)
        yield len(b)
        a.append(q)
A358127_list = list(islice(A358127_gen(),100)) # _Chai Wah Wu_, Nov 02 2022

