# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365517

from itertools import count, islice
from sympy.ntheory.primetest import is_square
from sympy import factorint
def A365517_gen(startvalue=1): # generator of terms >= startvalue
    for k in count(max(startvalue,1)):
        a, b = 1, 1
        for p, e in factorint(k).items():
            if e&1:
                a *= p
            else:
                b *= p
        if is_square(a*(b+1)):
            yield k
A365517_list = list(islice(A365517_gen(),30)) # _Chai Wah Wu_, Sep 19 2023

