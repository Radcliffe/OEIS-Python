# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A060019

from math import isqrt
from sympy import prime
def A060019(n): return isqrt(prime(n)-2<<2) # _Chai Wah Wu_, Jun 06 2025

