# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A291208

from math import prod
from sympy import factorint
def A291208(n):
    f = factorint(n).values()
    return prod(e+1 for e in f)-prod(e//3+1 for e in f) # _Chai Wah Wu_, Jun 05 2025

