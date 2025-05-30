# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A065824

from itertools import count
from math import prod
from sympy import factorint
def A065824(n):
    for m in count(1):
        f = factorint(m)
        if (n+1)*m*prod((p-1)**2 for p in f)==n*prod(p**(e+2)-p for p,e in f.items()):
            return m # _Chai Wah Wu_, Aug 12 2024

