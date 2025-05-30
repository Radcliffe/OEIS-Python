# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343997

from sympy.ntheory.modular import crt
from sympy import factorint
from itertools import product
def A343997(n):
    fs = factorint(2*n)
    plist = [p**fs[p] for p in fs]
    x = min(k for k in (crt(plist,d)[0] for d in product([0,-1],repeat=len(plist))) if k > 0)
    return x + x % 2 # _Chai Wah Wu_, Jun 01 2021

