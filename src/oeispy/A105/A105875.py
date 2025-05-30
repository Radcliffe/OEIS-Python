# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A105875

from sympy import n_order, nextprime
from itertools import islice
def A105875_gen(startvalue=2): # generator of terms >= startvalue
    p = max(startvalue-1,1)
    while (p:=nextprime(p)):
        if p!=3 and n_order(-3,p) == p-1:
            yield p
A105875_list = list(islice(A105875_gen(),20)) # _Chai Wah Wu_, Aug 11 2023

