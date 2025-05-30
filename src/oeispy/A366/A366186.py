# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366186

from itertools import count, islice
from sympy import Poly, diff, bernoulli
from sympy.abc import x
def A366186_gen(): # generator of terms
    return filter(lambda k:k<=3 or all(c.is_integer for c in Poly(diff(bernoulli(k,x),x,3)).coeffs()),count(1))
A366186_list = list(islice(A366186_gen(),30)) # _Chai Wah Wu_, Oct 03 2023

