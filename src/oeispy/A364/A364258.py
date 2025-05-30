# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364258

from sympy import nextprime
def A364258(n):
    c, p, k = 1, 1, n
    while k:
        c *= (p:=nextprime(p))**(s:=(~k&k-1).bit_length())
        k >>= s+1
    return c*p-n # _Chai Wah Wu_, Jul 25 2023

