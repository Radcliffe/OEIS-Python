# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A270807

from __future__ import division
from sympy import primefactors
A270807_list, b = [], 1
for i in range(10000):
    A270807_list.append(b)
    b += b//(max(primefactors(b)+[1])) + 1 # _Chai Wah Wu_, Apr 06 2016

