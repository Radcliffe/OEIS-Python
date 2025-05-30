# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A137595

from itertools import groupby
def ok(n):
    if n == 0: return False
    d = [len(list(g[1])) for g in groupby(bin(n)[2:])]
    d[-1] += 1
    return all(d[i]==d[-i-1] for i in range(len(d)//2))
print((str([n for n in range(100) if ok(n)]))) # _Dominic McCarty_, Mar 04 2025

