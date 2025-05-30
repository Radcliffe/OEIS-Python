# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068859

from itertools import islice
from sympy import sqrt_mod_iter
def A068859_gen(): # generator of terms
    a = 3
    while True:
        yield a
        b = a+1
        for d in sqrt_mod_iter(1,a):
            if d==1 or d**2-1 == a:
                d += a
            if d < b:
                b = d
        a = b**2-1
A068859_list = list(islice(A068859_gen(),11)) # _Chai Wah Wu_, May 05 2024

