# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A075904

A075904_list, m = [0], [24, -36, 14, -1, 0]
for n in range(1,10**9+1):
    for i in range(4):
        m[i+1] += m[i]
    if str(n) in str(m[-1]):
        A075904_list.append(n) # _Chai Wah Wu_, Nov 05 2014

