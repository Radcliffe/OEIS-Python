# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064614

from operator import mul
from functools import reduce
from sympy import factorint
def A064614(n):
    return reduce(mul,((5-p if 2<=p<=3 else p)**e for p,e in factorint(n).items())) if n > 1 else n
# _Chai Wah Wu_, Dec 27 2014

