# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A266148

from sympy import isprime
def A266148(n):
    return sum(1 for d in range(-9,1) for i in range(n) if isprime(10**n-1+d*10**i)) # _Chai Wah Wu_, Dec 31 2015

