# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A260728

from functools import reduce
from operator import or_
from sympy import factorint
def A260728(n): return reduce(or_,(e for p, e in factorint(n).items() if p & 3 == 3),0) # _Chai Wah Wu_, Jun 28 2022

