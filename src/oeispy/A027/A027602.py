# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A027602

A027602_list, m = [], [18, 0, 9, 9]
for _ in range(10**2):
    A027602_list.append(m[-1])
    for i in range(3):
        m[i+1] += m[i] # _Chai Wah Wu_, Dec 15 2015

