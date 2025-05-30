# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349161

from math import prod, gcd
from sympy import nextprime, factorint
def A349161(n):
    f = factorint(n).items()
    a = prod(nextprime(p)**e for p, e in f)
    b = prod((p**(e+1)-1)//(p-1) for p, e in f)
    return a//gcd(a,b) # _Chai Wah Wu_, Mar 17 2023

