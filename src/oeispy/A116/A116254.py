# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116254

from itertools import count, islice
from sympy import sqrt_mod
def A116254_gen(): # generator of terms
    for j in count(0):
        b = 10**j
        a = b*10+1
        for k in sorted(sqrt_mod(-1,a,all_roots=True)):
            m = (k**2+1)//a
            if a*(b+4) <= k**2+1 < a*(a+3):
                yield k-2
A116254_list = list(islice(A116254_gen(),40)) # _Chai Wah Wu_, Feb 19 2024

