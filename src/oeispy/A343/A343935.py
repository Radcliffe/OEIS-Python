# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343935

from math import comb
from sympy import divisor_count
def A343935(n): return comb(divisor_count(n)+n-1,n) # _Chai Wah Wu_, Jul 05 2024

