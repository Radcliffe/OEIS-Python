# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365068

from sympy.utilities.iterables import partitions
def A365068(n):
    if n <= 1: return 0
    alist, c = [set(tuple(sorted(set(p))) for p in partitions(i)) for i in range(n)], 0
    for p in partitions(n,k=n-1):
        s = set(p)
        if any(set(t).issubset(s-{q}) for q in s for t in alist[q]):
            c += 1
    return c # _Chai Wah Wu_, Sep 20 2023

