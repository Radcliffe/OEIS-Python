# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244915

from sympy import isprime
A244915 = [1]
blist = []
for n in range(1, 100):
    a, b = 1, 1 + A244915[-1]**2
    while not isprime(b) or b in blist:
        b += 2*a+1
        a += 1
    blist.append(b)
    A244915.append(a)
# _Chai Wah Wu_, Aug 28 2014

