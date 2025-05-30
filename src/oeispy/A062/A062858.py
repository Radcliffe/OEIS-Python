# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062858

from itertools import count
from collections import Counter
def A062858(n):
    c = Counter()
    for m in count(1):
        for i in range(1,m+1):
            ij = i*m
            c[ij] += 1
            if c[ij]>=n:
                return ij # _Chai Wah Wu_, Oct 16 2023

