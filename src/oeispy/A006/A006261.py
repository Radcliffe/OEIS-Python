# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A006261

A006261_list, m = [], [1, -3, 4, -2, 1, 1]
for _ in range(10**2):
    A006261_list.append(m[-1])
    for i in range(5):
        m[i+1] += m[i] # _Chai Wah Wu_, Jan 24 2016

