# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A335306

from sympy import prime, primefactors
def A335306(n):
    p = prime(n)
    for m in range(max(4,2*p-4),p**2+1):
        if sum(primefactors(m)) == p:
            return m # _Chai Wah Wu_, Jun 01 2020

