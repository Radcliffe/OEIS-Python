# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339507

from functools import lru_cache
from itertools import combinations
@lru_cache(maxsize=None)
def A339507(n):
    pallist = set(i for i in range(1,n*(n+1)//2+1) if str(i) == str(i)[::-1])
    return 1 if n == 0 else A339507(n-1) + sum(sum(d)+n in pallist for i in range(n) for d in combinations(range(1,n),i)) # _Chai Wah Wu_, Dec 08 2020

