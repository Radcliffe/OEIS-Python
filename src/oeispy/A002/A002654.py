# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A002654

from math import prod
from sympy import factorint
def A002654(n): return prod(1 if p == 2 else (e+1 if p % 4 == 1 else (e+1) % 2) for p, e in factorint(n).items()) # _Chai Wah Wu_, May 09 2022

