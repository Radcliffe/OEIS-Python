# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A271899

A271899_list, m = [], [88, -128, 61, -8]+[1]*5
for _ in range(100):
    A271899_list.append(m[-1])
    for i in range(8):
        m[i+1] += m[i] # _Chai Wah Wu_, Apr 16 2016

