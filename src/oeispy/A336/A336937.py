# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A336937

from sympy import divisor_sigma
def A336937(n): return (~(m:=int(divisor_sigma(n))) & m-1).bit_length() # _Chai Wah Wu_, Jul 01 2022

