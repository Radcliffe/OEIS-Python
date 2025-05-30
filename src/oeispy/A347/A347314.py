# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347314

from math import gcd
A347314_list, nset, m, c, j, i = [1], {1}, 2, 0, 2, 1
for _ in range(10**4):
    i += 1
    k = m
    while k == j or gcd(k,j) == 1 or k in nset:
        k += 1
    if i == k:
        A347314_list.append(i)
    j = k + 1
    nset.add(k)
    while m in nset:
        m += 1 # _Chai Wah Wu_, Sep 07 2021

