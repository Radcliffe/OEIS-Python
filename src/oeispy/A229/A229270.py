# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A229270

from sympy import isprime, factorint
A229270 = [n for n in range(1,10**5) if isprime(sum([int(n*e/p) for p,e in factorint(n).items()])-n)] # _Chai Wah Wu_, Aug 21 2014

