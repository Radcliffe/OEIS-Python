# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376114

from itertools import count, islice
from math import prod
from sympy import factorint
def A376114_gen(): # generator of terms
    for n in count(1):
        k = prod((e<<1|1)+(p==2) for p, e in factorint(n).items())
        if not (m:=n**2<<1)%k: yield m
A376114_list = list(islice(A376114_gen(),47)) # _Chai Wah Wu_, Oct 04 2024

