# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A298312

from __future__ import division
from sympy import prevprime, nextprime
A298312_list, n, m = [], 1, 30
while len(A298312_list) < 10000:
    k = prevprime(m//3)
    k2 = nextprime(k)
    if prevprime(k) + k + k2 == m or k + k2 + nextprime(k2) == m:
        A298312_list.append(n*(3*n-2))
    n += 1
    m += 18*n + 3 # _Chai Wah Wu_, Jan 22 2018

