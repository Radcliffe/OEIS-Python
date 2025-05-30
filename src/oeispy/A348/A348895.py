# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348895

from functools import lru_cache
from sympy.combinatorics.partitions import IntegerPartition
from sympy.utilities.iterables import partitions, multiset_permutations
@lru_cache(maxsize=None)
def intpartition(n,m): return tuple(''.join(str(d) for d in IntegerPartition(p).partition+[0]*(m-s)) for s, p in partitions(n,k=9,m=m,size=True))
def A348895(n):
    l, c, nmax, k = 9*n, 0, 0, 10**(n-1)
    while l > c:
        for p in intpartition(l,n):
            for q in multiset_permutations(p):
                w = int(''.join(q))
                if w >= k:
                    wr = w % l
                    if wr > c:
                        c = wr
                        nmax = w
                    if wr == c and nmax < w:
                        nmax = w
        l -= 1
    return nmax

