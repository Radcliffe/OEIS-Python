# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366750

from math import gcd
from sympy.utilities.iterables import partitions
def A366750(n): return sum(1 for p in partitions(n) if all(d==1 for d in p.values()) and all(d&1 for d in p) and gcd(*p)>1) # _Chai Wah Wu_, Nov 02 2023

