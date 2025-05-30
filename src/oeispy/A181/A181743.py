# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A181743

from itertools import count, islice
from sympy import isprime
def A181743_gen(): # generator of terms
    m = 2
    for t in count(1):
        r=1<<t-1
        for k in range(t-1,0,-1):
            if isprime(m-r-1):
                yield k
            r>>=1
        m<<=1
A181743_list=list(islice(A181743_gen(),30)) # _Chai Wah Wu_, Jul 08 2022

