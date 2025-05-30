# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361206

from sympy.ntheory import abundance
from itertools import count, filterfalse
def A361206_list(nmax):
    A,s = [],0
    for n in range(1,nmax+1):
        A2 = set(A)
        for y in filterfalse(A2.__contains__,count(1)):
            ab = abundance(y)
            if ab != 0 and ab + s >= 1:
                A.append(y)
                s += ab
                break
    return(A)

