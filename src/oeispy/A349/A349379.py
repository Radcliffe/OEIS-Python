# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349379

from math import prod
from sympy import factorint
def A349379(n): return prod(0 if e==1 else p**e - (1 if e==2 else p**(e-1)) for p,e in factorint(n).items()) # _Chai Wah Wu_, Nov 14 2022

