# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A050999

from sympy import divisor_sigma
def A050999(n): return int(divisor_sigma(n>>(~n&n-1).bit_length(),2)) # _Chai Wah Wu_, Jul 16 2022

