# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A002219

from itertools import combinations_with_replacement
from sympy.utilities.iterables import partitions
def A002219(n): return len({tuple(sorted((p+q).items())) for p, q in combinations_with_replacement(tuple(Counter(p) for p in partitions(n)),2)}) # _Chai Wah Wu_, Sep 20 2023

