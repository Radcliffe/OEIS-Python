# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A209284

from itertools import product
def R(w):
    for l in range(len(w)):
        found = False
        for i in range(len(w)-l):
            f = w[i:i+l]
            if f+"0" in w and f+"1" in w: found = True; break
            if found: break
        if not found: return l
def H(w):
    for l in range(1, len(w)):
        prefix = w[:l]
        if "0"+prefix not in w and "1"+prefix not in w: return l
    return len(w)
def S(w): return R(w) < H(w)
def a(n):
    return 2*sum(1 for w in product("01", repeat=n-1) if S("0"+"".join(w)))
print([a(n) for n in range(1, 16)]) # _Michael S. Branicky_, Mar 21 2022

