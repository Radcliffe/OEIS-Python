# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384554

from math import prod
from sympy import factorint
def A384554(n): return prod((1,p+1,p**2+1,p*(p+1)+1)[e&3] for p,e in factorint(n).items()) # _Chai Wah Wu_, Jun 03 2025

