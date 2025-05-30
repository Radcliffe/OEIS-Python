# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A251411

from math import gcd
A251411_list, l1, l2, s, b = [1,2,3], 3, 2, 4, {}
for n in range(4,10**4):
    i = s
    while True:
        if not i in b and gcd(i,l1) == 1 and gcd(i,l2) > 1:
            l2, l1, b[i] = l1, i, 1
            while s in b:
                b.pop(s)
                s += 1
            if i == n:
                A251411_list.append(n)
            break
        i += 1 # _Chai Wah Wu_, Dec 03 2014

