# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280879

from sympy import totient
A280879_list, n, t = [], 1, 1
while len(A280879_list) < 1000:
    n += 1
    h = totient(n)
    t2 = t+h
    if n % 2 and n % 6 != 3 and 2*(n*(h*n - 2*t2 + 1) + t2) <  1:
        A280879_list.append(n)
    t = t2 # _Chai Wah Wu_, Feb 11 2017

