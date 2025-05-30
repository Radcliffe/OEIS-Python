# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367222

from itertools import combinations
from sympy.utilities.iterables import partitions
def A367222(n):
    c, mlist = 1, []
    for m in range(1,n+1):
        t = set()
        for p in partitions(m):
            t.add(tuple(sorted(p.keys())))
        mlist.append([set(d) for d in t])
    for k in range(1,n+1):
        for w in combinations(range(1,n+1),k):
            ws = set(w)
            for s in mlist[k-1]:
                if s <= ws:
                    c += 1
                    break
    return c # _Chai Wah Wu_, Nov 16 2023

