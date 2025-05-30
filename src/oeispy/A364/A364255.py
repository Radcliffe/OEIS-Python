# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364255

from math import gcd
from sympy import nextprime
def A364255(n):
    c, p, k = 1, 1, n
    while k:
        c *= (p:=nextprime(p))**(s:=(~k&k-1).bit_length())
        k >>= s+1
    return gcd(c*p,n) # _Chai Wah Wu_, Jul 25 2023

