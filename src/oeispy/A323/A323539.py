# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A323539

from itertools import product
def a(n): return len(set(tuple(l for l in range(n//2) if w[l] == "0" and w[:l] == w[l+1:2*l+1]) for w in product("01", repeat=n-1)))
print([a(n) for n in range(1, 22)]) # _Michael S. Branicky_, Jul 23 2022

