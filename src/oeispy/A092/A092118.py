# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A092118

from itertools import count, islice
from sympy import sqrt_mod
def A092118_gen(): # generator of terms
    for j in count(0):
        b = 10**j
        a = b*10+1
        ab, aa = a*b, a*(a-1)
        for k in sorted(sqrt_mod(0,a,all_roots=True)):
            if ab <= (m:=k**2) < aa:
                yield m
A092118_list = list(islice(A092118_gen(),10)) # _Chai Wah Wu_, Mar 06 2024

