# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061076

from math import prod
def A061076(n): return sum(prod(int(d) for d in str(i)) for i in range(1,n+1)) # _Chai Wah Wu_, Mar 21 2022

