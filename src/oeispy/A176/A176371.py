# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A176371

from sympy import isprime
A176371_list, i, j = [], 0, 13
while j < 10**10:
    p = int(str(j)[::-1])
    if j % 10 and isprime(p):
        A176371_list.append(p)
    j += 2*i+1
    i += 1
A176371_list = sorted(A176371_list) # _Chai Wah Wu_, Dec 17 2015

