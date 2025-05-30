# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353459

from math import prod
from sympy import factorint, primepi
def A353459(n):
    f = [(primepi(p)&1, -int(e==1)) for p, e in factorint(n).items()]
    return prod(e for p, e in f if not p)+prod(e for p, e in f if p) # _Chai Wah Wu_, Jan 05 2023

