# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064113

from itertools import count, islice
from sympy import prime, nextprime
def A064113_gen(startvalue=1): # generator of terms >= startvalue
    c = max(startvalue,1)
    p = prime(c)
    q = nextprime(p)
    r = nextprime(q)
    for k in count(c):
        if p+r==(q<<1):
            yield k
        p, q, r = q, r, nextprime(r)
A064113_list = list(islice(A064113_gen(),20)) # _Chai Wah Wu_, Feb 27 2024

