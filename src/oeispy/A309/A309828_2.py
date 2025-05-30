# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A309828

from itertools import count, islice
from sympy.ntheory.primetest import is_square
def A309828_gen(): # generator of terms
    return filter(is_square,(int(str(k)+str((k<<1)+1)) for k in count(1)))
A309828_list = list(islice(A309828_gen(),20)) # _Chai Wah Wu_, Feb 20 2023

