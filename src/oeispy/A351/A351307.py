# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351307

from math import prod
from sympy import factorint
def A351307(n): return prod((p**(4+((e&-2)<<1))-1)//(p**4-1) for p,e in factorint(n).items()) # _Chai Wah Wu_, Jul 11 2024

