# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A057661

from math import lcm
def A057661(n): return sum(lcm(n,k)//n for k in range(1,n+1)) # _Chai Wah Wu_, Aug 24 2023

