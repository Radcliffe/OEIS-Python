# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A007426

from math import prod, comb
from sympy import factorint
def A007426(n): return prod(comb(3+e,3) for e in factorint(n).values()) # _Chai Wah Wu_, Dec 22 2024

