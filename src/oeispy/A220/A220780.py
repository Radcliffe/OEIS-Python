# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A220780

from sympy import harmonic
def A220780(n): return (~(m:=int(harmonic(k:=(n<<1)+(n&1),-k)))&m-1).bit_length() # _Chai Wah Wu_, Jul 11 2022

