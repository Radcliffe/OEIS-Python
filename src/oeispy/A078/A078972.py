# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A078972

from sympy import sieve
A078972 = []
for n in range(3):
    pr = list(sieve.primerange(10**n,10**(n+1)))
    for i,p in enumerate(pr):
        for q in pr[i:]:
            A078972.append(p*q)
A078972 = sorted(A078972)
# _Chai Wah Wu_, Aug 26 2014

