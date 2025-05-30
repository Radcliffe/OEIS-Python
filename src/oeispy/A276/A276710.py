# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A276710

from itertools import islice
from math import comb
from sympy import nextprime
def A276710_gen(): # generator of terms
    p, q = 3, 5
    while True:
        for m in range(p+1,q):
            r = m**(m-1)
            c = 1
            for k in range(m+1):
                c = c*comb(m,k) % r
            if c == 0:
                yield m
        p, q = q, nextprime(q)
A276710_list = list(islice(A276710_gen(),40)) # _Chai Wah Wu_, Jun 08 2022

