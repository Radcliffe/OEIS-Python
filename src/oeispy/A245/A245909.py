# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A245909

from sympy import primefactors,prime
def A245909(n):
    return len(primefactors(prime(n)**3-1)) # _Chai Wah Wu_, Aug 05 2014

