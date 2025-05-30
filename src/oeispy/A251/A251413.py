# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A251413

from math import gcd
A251413_list, l1, l2, s, b = [1,3,5], 5, 3, 7, {}
for _ in range(1,10**4):
    i = s
    while True:
        if not i in b and gcd(i,l1) == 1 and gcd(i,l2) > 1:
            A251413_list.append(i)
            l2, l1, b[i] = l1, i, True
            while s in b:
                b.pop(s)
                s += 2
            break
        i += 2 # _Chai Wah Wu_, Dec 07 2014

