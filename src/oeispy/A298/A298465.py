# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A298465

from sympy import prevprime, nextprime
A298465_list, n, m = [], 1 ,8
while len(A298465_list) < 10000:
    k = prevprime(m//2)
    if k + nextprime(k) == m:
        A298465_list.append(n*(5*n-3)//2)
    n += 1
    m += 10*n-3 # _Chai Wah Wu_, Jan 19 2018

