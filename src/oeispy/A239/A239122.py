# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A239122

from functools import reduce
from operator import ixor
from sympy import factorint
def A239122(n): return sum(-i if reduce(ixor, factorint(i).values(), 0)&1 else i for i in range(1,n+1)) # _Chai Wah Wu_, Jan 03 2023

