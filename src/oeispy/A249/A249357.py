# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A249357

from math import gcd
A249357_list, l1, l2 = [1,2,3], 3, 2
for _ in range(100):
    i = l1+l2
    while True:
        if gcd(i,l1) == 1 and gcd(i,l2) > 1:
            A249357_list.append(i)
            l2, l1 = l1, i
            break
        i += 1 # _Chai Wah Wu_, Dec 04 2014

