# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A056626

from math import prod
from sympy import factorint
def A056626(n):
    f = factorint(n).values()
    return prod((e>>1)+1 for e in f)-(1<<sum(e&1^1 for e in f)) # _Chai Wah Wu_, Aug 04 2024

