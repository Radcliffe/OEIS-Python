# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A240851

from sympy.utilities.iterables import partitions
def A240851(n): return sum(1 for s,p in partitions(n,size=True) if max(p.values(),default=0)==1 and (n%s or n//s not in p)) # _Chai Wah Wu_, Sep 21 2023

