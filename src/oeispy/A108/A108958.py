# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A108958

from math import comb
def A108958(n): return comb((n<<1)-1,n-1)-(1<<n-1) # _Chai Wah Wu_, Sep 23 2022

