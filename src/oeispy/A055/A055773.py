# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055773

from math import prod
from sympy import primerange
def A055773(n): return prod(primerange((n>>1)+1,n+1)) # _Chai Wah Wu_, Apr 13 2024

