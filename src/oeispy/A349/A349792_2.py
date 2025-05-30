# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349792

from itertools import count, islice
from sympy import primepi, prime, nextprime
def A349792gen(): # generator of terms
    p1 = 0
    for n in count(1):
        p2 = primepi((n+1)**2)
        b = p1 + p2 + 1
        if b % 2:
            p = prime(b//2)
            q = nextprime(p)
            if p+q == 2*n*(n+1):
                yield n
        p1 = p2
A349792_list = list(islice(A349792gen(),12)) # _Chai Wah Wu_, Dec 08 2021

