# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365631

from sympy.utilities.iterables import partitions
def A365631(n): return sum(1 for p in partitions(n) if len(p)==5) # _Chai Wah Wu_, Sep 14 2023

