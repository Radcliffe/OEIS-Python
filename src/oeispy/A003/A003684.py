# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A003684

from sympy import primerange, isprime
def A003684(n):
    return len([p for p in primerange(10**(n-1),10**n)
    if len(set(str(p))) == len(str(p)) and isprime(int(str(p)[::-1]))])
# _Chai Wah Wu_, Aug 14 2014

