# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A058995

from sympy import isprime
k, m, A058995_list = 1, 13,  []
while k <= 10**3:
    if isprime(int(str(m)[::-1])):
        A058995_list.append(k)
    k += 1
    m *= 13 # _Chai Wah Wu_, Mar 09 2021

