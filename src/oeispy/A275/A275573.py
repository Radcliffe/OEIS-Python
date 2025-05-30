# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A275573

from __future__ import division
from fractions import Fraction
A275573_list, q = [], 0
for i in range(1,10**6):
    q += Fraction(int(str(i)[::-1]),10**len(str(i)))
    if q.denominator == 1:
        A275573_list.append(q + i*(i+1)//2) # _Chai Wah Wu_, Aug 24 2016

