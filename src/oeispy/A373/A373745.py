# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373745

from sympy import prime
def A373745(n):
    s = bin(prime(n))[2:]
    return next(i for i in range(len(s),0,-1) if ('01'*(i+1>>1))[:i] in s or ('10'*(i+1>>1))[:i] in s) # _Chai Wah Wu_, Jul 10 2024

