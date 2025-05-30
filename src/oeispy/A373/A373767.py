# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373767

from itertools import count, islice
from sympy.ntheory.primetest import is_square
def A373767_gen(): # generator of terms
    k, c = 0, 0
    for i in count(1):
        for n in range(i**3+1,(i+1)**3):
            k += 1
            c += n
            if is_square(c):
                yield k
A373767_list = list(islice(A373767_gen(),20)) # _Chai Wah Wu_, Jun 18 2024

