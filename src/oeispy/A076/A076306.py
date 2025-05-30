# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A076306

from __future__ import division
from sympy import nextprime, prevprime, isprime
A070306_list, i = [], 3
while i < 10**6:
    n = i**3
    m = n//3
    pm, nm = prevprime(m), nextprime(m)
    k = n - pm - nm
    if isprime(m):
        if m == k:
            A070306_list.append(i)
    else:
        if nextprime(nm) == k or prevprime(pm) == k:
            A070306_list.append(i)
    i += 1 # _Chai Wah Wu_, May 30 2017

