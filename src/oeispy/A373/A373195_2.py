# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373195

from math import prod
from itertools import combinations
from functools import lru_cache
from sympy.ntheory.primetest import is_square
@lru_cache(maxsize=None)
def A373195(n):
    if n==1: return 1
    i = A373195(n-1)+1
    if sum(1 for p in combinations(range(1,n),5) if is_square(n*prod(p))) > 0:
        a = [set(p) for p in combinations(range(1,n+1),6) if is_square(prod(p))]
        for q in combinations(range(1,n),i-1):
            t = set(q)|{n}
            if not any(s<=t for s in a):
                return i
        else:
            return i-1
    else:
        return i # _Chai Wah Wu_, May 30 2024

