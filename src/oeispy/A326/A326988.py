# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A326988

from sympy import divisor_sigma
def A326988(n): return divisor_sigma(n)-(n^(n-1)) # _Chai Wah Wu_, Aug 04 2022

