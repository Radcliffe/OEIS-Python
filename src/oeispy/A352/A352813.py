# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352813

from math import prod, factorial
from itertools import combinations
def A352813(n):
    m = factorial(2*n)
    return 0 if n == 0 else min(abs((p:=prod(d))-m//p) for d in combinations(range(2,2*n+1),n-1)) # _Chai Wah Wu_, Apr 06 2022

