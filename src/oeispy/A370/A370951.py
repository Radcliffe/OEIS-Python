# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370951

from itertools import count, islice
from sympy import nextprime
def A370951_gen(): # generator of terms
    a, aset, p, q = 1, {1}, 2, 0
    for c in count(2):
        if (b:=a-p) > 0 and b not in aset:
            a = b
        elif (b:=a+p) not in aset:
            a = b
        else:
            a = 0
            if q:
                yield c-q
            q = c
        aset.add(a)
        p = nextprime(p)
A370951_list = list(islice(A370951_gen(),10)) # _Chai Wah Wu_, Mar 07 2024

