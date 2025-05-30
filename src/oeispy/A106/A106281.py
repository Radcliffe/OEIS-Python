# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A106281

from itertools import islice
from sympy import Poly, nextprime
from sympy.abc import x
def A106281_gen(): # generator of terms
    p = 2
    while True:
        if len(Poly(x*(x*(x*(x*(x-1)-1)-1)-1)-1, x, modulus=p).ground_roots())==5:
            yield p
        p = nextprime(p)
A106281_list = list(islice(A106281_gen(),20)) # _Chai Wah Wu_, Mar 14 2024

