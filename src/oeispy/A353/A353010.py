# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353010

from math import prod, comb
from itertools import islice
from sympy import nextprime
def A353010_gen(): # generator of terms
    p, q = 3, 5
    while True:
        for m in range(p+1,q):
            r = m**(m-1)
            c = 1
            for k in range(m+1):
                c = c*comb(m,k) % r
            if c == 0:
                d, (e, f) = -m, divmod(prod(comb(m,k) for k in range(m+1)),m)
                while f == 0:
                    d += 1
                    e, f = divmod(e,m)
                yield d
        p, q = q, nextprime(q)
A353010_list = list(islice(A353010_gen(),40)) # _Chai Wah Wu_, Jun 09 2022

