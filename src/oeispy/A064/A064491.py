# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064491

from itertools import islice
from sympy import divisor_count
def A064491gen(): # generator of terms
    n = 1
    yield n
    while True:
        n += divisor_count(n)
        yield n
A064491_list = list(islice(A064491gen(),20)) # _Chai Wah Wu_, Dec 13 2021

