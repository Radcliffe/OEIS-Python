# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A295294

from math import prod
from sympy import factorint
def A295294(n): return prod((p**(e+1)-1)//(p-1) for p, e in factorint(n).items() if e > 1) # _Chai Wah Wu_, Nov 14 2022

