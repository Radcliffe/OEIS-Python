# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A100682

from math import comb
from sympy import integer_nthroot
def A100682(n): return integer_nthroot(comb(n+3,4),4)[0] # _Chai Wah Wu_, Oct 02 2024

