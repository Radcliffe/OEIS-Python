# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A031219

from itertools import count, chain, islice
from sympy.ntheory.factor_ import digits
def A031219_gen(): return chain.from_iterable(digits(m, 5)[1:] for m in count(1))
A031219_list = list(islice(A031219_gen(), 30)) # _Chai Wah Wu_, Jan 07 2022

