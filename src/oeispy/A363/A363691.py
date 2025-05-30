# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363691

from itertools import count, islice
from sympy import divisors
def A363691_gen(startvalue=3): # generator of terms >= startvalue
    return filter(lambda n:all(d==1 or d==n or n|d!=n for d in divisors(n,generator=True)),count(max(startvalue,3)|1,2))
A363691_list = list(islice(A363691_gen(),20)) # _Chai Wah Wu_, Jun 20 2023

