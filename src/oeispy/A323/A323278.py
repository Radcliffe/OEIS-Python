# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A323278

from sympy import divisor_count, nextprime
A323278_list, p, nmax = [], 2 , -1
while len(A323278_list) < 100:
    n = divisor_count(p**2-1)
    if n > nmax:
        nmax = n
        A323278_list.append(p**2-1)
    p = nextprime(p) # _Chai Wah Wu_, Feb 09 2019

