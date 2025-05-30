# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A185635

from math import gcd
A185635_list, l1, l2, m, b = [1, 2], 2, 1, 2, {1, 2}
for n in range(3, 10**4):
    i = m
    while True:
        if not i in b:
            if n == i:
                A185635_list.append(i)
            l1, l2, m = i, l1, i//gcd(l1, i)
            b.add(i)
            break
        i += m # _Chai Wah Wu_, Dec 09 2014

