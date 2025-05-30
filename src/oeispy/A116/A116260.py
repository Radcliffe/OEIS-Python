# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116260

from itertools import count, islice
from sympy import sqrt_mod
def A116260_gen(): # generator of terms
    for j in count(0):
        b = 10**j
        a = b*10+1
        for k in sorted(sqrt_mod(0,a,all_roots=True))+[a]:
            if a*(b+4) <= k**2 < a*(a+3):
                yield k-2
A116260_list = list(islice(A116260_gen(),20)) # _Chai Wah Wu_, Feb 19 2024

