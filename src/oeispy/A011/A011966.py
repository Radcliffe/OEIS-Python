# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A011966

# requires python 3.2 or higher. Otherwise use def'n of accumulate in python docs.
from itertools import accumulate
A011966_list, blist, b = [1], [2, 3, 5], 5
for _ in range(1000):
    blist = list(accumulate([b]+blist))
    b = blist[-1]
    A011966_list.append(blist[-4]) # _Chai Wah Wu_, Sep 20 2014

