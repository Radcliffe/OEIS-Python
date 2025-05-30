# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A057630

from sympy import isprime, nextprime
A057630_list, dlist, p = [], [str(d)*d for d in range(10)], 2
while len(A057630_list) < 10000:
    if isprime(int(''.join(dlist[int(d)] for d in str(p)))):
        A057630_list.append(p)
    p = nextprime(p) # _Chai Wah Wu_, Dec 19 2019, corrected Jan 01 2022

