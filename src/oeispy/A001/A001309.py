# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001309

from math import prod
def A001309(n): return 2 if n == 0 else ((1<<n)-1)*prod((1<<i)-1 for i in range(2,2*n-1,2)) << n*(n+1)+2 # _Chai Wah Wu_, Jun 20 2022

