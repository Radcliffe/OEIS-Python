# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363735

from sympy import divisor_count
def A363735(n): return n*(n+1)-(n-1)*divisor_count(n) if n else 1 # _Chai Wah Wu_, Jun 28 2023

