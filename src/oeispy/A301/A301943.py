# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A301943

from sympy import isprime
def A301943(n):
    return sum(1 for i in range(1,10**(n-1)+1) if isprime(100*i**2+1)) # _Chai Wah Wu_, Mar 30 2018

