# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A088887

from sympy.utilities.iterables import partitions
def A088887(n): return len({tuple(sorted(p.values())) for p in partitions(n)}) # _Chai Wah Wu_, Sep 10 2023

