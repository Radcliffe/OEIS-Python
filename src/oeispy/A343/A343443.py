# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343443

from math import prod
from sympy import factorint
def A343443(n): return prod(e+2 for e in factorint(n).values()) # _Chai Wah Wu_, Feb 21 2025

