# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A227349

from operator import mul
from functools import reduce
from re import split
def A227349(n):
    return reduce(mul, (len(d) for d in split('0+',bin(n)[2:]) if d)) if n > 0 else 1 # _Chai Wah Wu_, Sep 07 2014

