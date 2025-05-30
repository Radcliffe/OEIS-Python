# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357356

from functools import lru_cache
def cond(s, c): q, r = divmod(s, c); return r == 0 and q&1 == 0
@lru_cache(maxsize=None)
def b(n, s, c):
    if n == 0: return int (c > 0 and cond(s, c))
    return b(n-1, s, c) + b(n-1, s+n, c+1)
a = lambda n: b(n, 0, 0)
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Sep 25 2022

