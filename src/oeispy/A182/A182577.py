# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A182577

from math import factorial
def A182577(n):
    m, tlist, s = factorial(n), [1,2], 0
    while tlist[-1]+tlist[-2] <= m:
        tlist.append(tlist[-1]+tlist[-2])
    for d in tlist[::-1]:
        if d <= m:
            s += 1
            m -= d
    return s # _Chai Wah Wu_, Jun 15 2018

