# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A261182

from gmpy2 import is_prime
from itertools import product
A261182_list = [int(''.join(d)) for l in range(1,10) for d in product('279',repeat=l) if is_prime(int(''.join(d)))] # _Chai Wah Wu_, Aug 11 2015

