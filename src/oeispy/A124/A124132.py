# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A124132

from itertools import count, islice
from sympy import factorint, fibonacci
def A124132_gen(): # generator of terms
    return filter(lambda n:all(p & 3 != 3 or e & 1 == 0 for p, e in factorint(fibonacci(2*n)).items()),count(1))
A124132_list = list(islice(A124132_gen(),10)) # _Chai Wah Wu_, Jun 27 2022

