# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A117129

from itertools import count, islice
from sympy import nextprime
def A117129_gen(): # generator of terms
    a, aset, p = 1, {1}, 2
    for c in count(2):
        if (b:=a-p) > 0 and b not in aset:
            a = b
        elif (b:=a+p) not in aset:
            a = b
        else:
            a = 0
            yield p
        aset.add(a)
        p = nextprime(p)
A117129_list =  list(islice(A117129_gen(),10)) # _Chai Wah Wu_, Mar 04 2024

