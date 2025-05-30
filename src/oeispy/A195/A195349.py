# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A195349

from sympy import divisor_count
A195349_list, s, p = [], 0, 1
for k in range(1,10**4):
    d = divisor_count(k)
    s += d
    p *= d
    if p % s == 0:
        A195349_list.append(k) # _Chai Wah Wu_, Oct 09 2021

