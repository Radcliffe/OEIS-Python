# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A053872

from sympy import isprime
A053872_list, n, m, s = [], 1, 4, 4
while len(A053872_list) < 10000:
    if isprime(s):
        A053872_list.append(s)
    m += 1
    if isprime(m):
        m += 1
    n += 1
    s += m # _Chai Wah Wu_, May 13 2018

