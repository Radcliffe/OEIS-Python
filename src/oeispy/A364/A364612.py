# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364612

from collections import Counter
from itertools import combinations
from sympy.utilities.iterables import partitions
def A364612(n): return sum(1 for p in partitions(n) if max(list(Counter(abs(d[0]-d[1]) for d in combinations(list(Counter(p).elements()),2)).values()),default=1)>1) # _Chai Wah Wu_, Sep 17 2023

