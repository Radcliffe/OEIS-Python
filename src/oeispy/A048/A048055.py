# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A048055

from sympy import divisors, primefactors
A048055 = []
for n in range(1,10**4):
    s = sum(divisors(n))
    if not s % 2 and 2*n <= s and (s-2*n)/2 == sum(primefactors(n)):
        A048055.append(n) # _Chai Wah Wu_, Aug 20 2014

