# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A051802

from operator import mul
from functools import reduce
def A051802(n):
    if n == 0:
        return 1
    while n > 9:
        n = reduce(mul, (int(d) for d in str(n) if d != '0'))
    return n
# _Chai Wah Wu_, Aug 23 2014

