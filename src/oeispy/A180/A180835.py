# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180835

from itertools import product
def d(s, k): return False if k == 0 else int("".join(s), 2)%k == 0
def T(n, k): return sum(1 for b in (b for b in product("01", repeat=n)) if not any(d(b[:i], k) for i in range(1, n+1)))
def auptodiag(maxd): return [T(d+1-j, j) for d in range(1, maxd+1) for j in range(d, 0, -1)]
print(auptodiag(14)) # _Michael S. Branicky_, Jun 09 2022

