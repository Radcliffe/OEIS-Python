# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000846

from math import comb
def A000846(n): return comb(3*n,n)-comb(n<<1,n) # _Chai Wah Wu_, Sep 07 2022

