# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340431

from sympy import nextprime
A340431_list , p = [], 2
while p <= 10**10:
    q = nextprime(p)
    if q > p+2:
        pq = p+q
        if pow(q,p,pq) == q and pow(p,q,pq) == p:
            A340431_list.append(p)
    p = q # _Chai Wah Wu_, Jan 12 2021

