# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A065619

from itertools import accumulate
def A065619(n):
    if n <= 2: return n
    blist = (0,1)
    for _ in range(n-2):
        blist = tuple(accumulate(reversed(blist),initial=0))
    return blist[-1]*n # _Chai Wah Wu_, Apr 25 2023

