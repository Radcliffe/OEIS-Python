# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A036347

from itertools import count, islice
from functools import reduce
from operator import ixor
from sympy import factorint
def A036347_gen(startvalue=1): # generator of terms
    return filter(lambda n:(reduce(ixor,(p*e for p, e in factorint(n).items()),0)^n)&1, count(max(startvalue,1)))
A036347_list = list(islice(A036347_gen(),20)) # _Chai Wah Wu_, Jan 15 2023

