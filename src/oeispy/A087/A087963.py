# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A087963

from sympy import prime
def A087963(n): return (~(m:=prime(n)*3+1)&m-1).bit_length() # _Chai Wah Wu_, Jul 10 2022

