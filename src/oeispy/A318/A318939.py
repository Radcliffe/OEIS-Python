# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A318939

from sympy import divisor_sigma
def A318939(n): return 3*(1+12*((1<<(3*(m:=(~n&n-1).bit_length())+3))-1)//7)*divisor_sigma(n>>m,3)<<4 if n else 1 # _Chai Wah Wu_, Jul 11 2022

