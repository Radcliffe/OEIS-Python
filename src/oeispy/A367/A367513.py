# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367513

from math import prod
from sympy import factorint
def A367513(n): return prod(p**e for p, e in factorint(n).items() if e.bit_count()&1^1) # _Chai Wah Wu_, Nov 23 2023

