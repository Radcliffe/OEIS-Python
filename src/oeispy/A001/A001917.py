# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001917

from sympy import prime, n_order
def A001917(n):
    p = prime(n)
    return 1 if n == 2 else (p-1)//n_order(2,p) # _Chai Wah Wu_, Jan 15 2020

