# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366442

from sympy import divisor_sigma
def A366442(n): return divisor_sigma((n+(n>>1)<<1)-1) # _Chai Wah Wu_, Oct 10 2023

