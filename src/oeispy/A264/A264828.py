# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A264828

from itertools import count, islice
from sympy import isprime
def A264828_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:not (isprime(n) or (n&1^1 and isprime(n>>1))),count(max(startvalue,1)))
A264828_list = list(islice(A264828_gen(),20)) # _Chai Wah Wu_, Mar 26 2024

