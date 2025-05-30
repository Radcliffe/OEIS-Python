# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339149

from itertools import product
def sc(v):
    best = 0
    for y in (v[-i:] for i in range(1, len(v)//2+1)):
        for t in range(2, len(v)//len(y)+1):
            if not v.endswith(y*t): break
            best = max(best, (t-1)*len(y))
    return best
def a(n): # by symmetry, twice that of starting with "0"
    return 2*sum(sc("0"+"".join(b)) for b in product("01", repeat=n-1))
print([a(n) for n in range(1,21)]) # _Michael S. Branicky_, Nov 28 2020

