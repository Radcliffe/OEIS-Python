# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A011965

# requires python 3.2 or higher. Otherwise use def'n of accumulate in python docs.
from itertools import accumulate
A011965_list, blist, b = [1], [1, 2], 2
for _ in range(1000):
    blist = list(accumulate([b]+blist))
    b = blist[-1]
    A011965_list.append(blist[-3])
# _Chai Wah Wu_, Sep 02 2014

