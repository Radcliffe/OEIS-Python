# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358565

from itertools import islice
from sympy import isprime
def A358565_gen(): # generator of terms
    p, q = 5, 11
    while True:
        while not isprime(q):
            q += 3
        yield (q-p)//6
        p = q
        q += 3
A358565_list = list(islice(A358565_gen(),30)) # _Chai Wah Wu_, Jan 05 2023

