# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A080378

from sympy import prime
def A080378(n): return (prime(n+1)-prime(n))&3 # _Chai Wah Wu_, Jul 07 2022

