# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A229272

from sympy import isprime, factorint
A229272 = []
for n in range(1, 10**5):
    np = sum([int(n*e/p) for p, e in factorint(n).items()]) if n > 1 else 0
    if isprime(np+n) and isprime(np-n):
        A229272.append(n)
# _Chai Wah Wu_, Aug 21 2014

