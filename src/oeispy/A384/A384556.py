# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384556

from math import prod
from sympy import factorint
def A384556(n): return prod(p*(1+p*(e&1^1)) for p, e in factorint(n).items()) # _Chai Wah Wu_, Jun 03 2025

