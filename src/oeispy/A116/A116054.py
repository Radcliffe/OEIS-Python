# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116054

from sympy import nextprime
n, k, m, A116054_list = 0, 1, 2, []
while len(A116054_list) < 100:
    for i in range(k,m):
        s = str(i*n)
        if s == s[::-1]:
            A116054_list.append(i)
    n += 1
    k, m = m, nextprime(m) # _Chai Wah Wu_, Jul 25 2018

