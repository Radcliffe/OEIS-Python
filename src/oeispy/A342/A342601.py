# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342601

A342601_list, k, m, s = [], 1, 2, str(2**10)
while k < 10**6:
    if s in str(m):
        A342601_list.append(k)
    k += 1
    m *= 2 # _Chai Wah Wu_, Mar 17 2021

