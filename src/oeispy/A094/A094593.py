# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A094593

from sympy import prime, n_order
def A094593(n):
    p = prime(n)
    return 1 if n == 3 else (p-1)//n_order(3,p) # _Chai Wah Wu_, Jan 15 2020

