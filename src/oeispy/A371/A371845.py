# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371845

from itertools import count, islice
from sympy import primerange
def A371845_gen(): # generator of terms
    for l in count(1):
        m = 10**l
        for a in range(1,10):
            b = (a*10**4+2345)*m
            yield from primerange(b,b+m)
A371845_list = list(islice(A371845_gen(),20)) # _Chai Wah Wu_, Apr 09 2024

