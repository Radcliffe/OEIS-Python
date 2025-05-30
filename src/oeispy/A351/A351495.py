# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351495

from itertools import count, islice
from sympy import prime, primepi, primefactors
def A351495_gen(): # generator of terms
    aset, cset = set(), {1}
    yield 1
    while True:
        for i in count(1):
            if not i in aset:
                p = prime(i)
                for j in count(1):
                    if (m:=j*p) not in cset:
                        yield m
                        cset.add(m)
                        break
                break
        aset = set(map(primepi,primefactors(m)))
A351495_list = list(islice(A351495_gen(),30)) # _Chai Wah Wu_, Mar 18 2023

