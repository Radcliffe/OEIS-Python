# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A305444

from math import prod
from sympy import primefactors
def A305444(n): return prod(p-2 for p in primefactors(n>>(~n&n-1).bit_length())) # _Chai Wah Wu_, Sep 08 2023

