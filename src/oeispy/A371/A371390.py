# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371390

from itertools import count, islice
from sympy import nextprime
def A371390_gen(): # generator of terms
    xlist, p = [2, 3, 5, 7, 1], 11
    for k in count(1):
        if len(set(xlist)) == 1:
            yield k
        p = nextprime(p)
        xlist = xlist[1:]+[p%10]
A371390_list = list(islice(A371390_gen(),10)) # _Chai Wah Wu_, Apr 13 2024

