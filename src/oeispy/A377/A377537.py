# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377537

from math import comb
from sympy import primepi
def A377537(n): return comb(primepi(n)+n-1,n) # _Chai Wah Wu_, Nov 12 2024

