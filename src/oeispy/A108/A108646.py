# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A108646

A108646_list, m = [], [77, -85, 28, -1, 1, 1, 1, 1]
for _ in range(10001):
    A108646_list.append(m[-1])
    for i in range(7):
        m[i+1] += m[i] # _Chai Wah Wu_, Jun 12 2016

