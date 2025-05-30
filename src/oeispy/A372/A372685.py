# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372685

from itertools import islice
from sympy import nextprime
def A372685_gen(): # generator of terms
    p, a = 1, {}
    while (p:=nextprime(p)):
        if (c:=p.bit_count()) not in a:
            yield p
        a[c] = p
A372685_list = list(islice(A372685_gen(),20)) # _Chai Wah Wu_, May 12 2024

