# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A090770

from math import prod
def A090770(n): return prod((1<<i)-1 for i in range(2,2*n+1,2)) << (n+1)**2 # _Chai Wah Wu_, Jun 20 2022

