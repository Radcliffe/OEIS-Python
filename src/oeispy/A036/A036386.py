# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A036386

from sympy import primepi, integer_nthroot
def A036386(n):
    m = 1<<n
    return sum(primepi(integer_nthroot(m,j)[0]) for j in range(2,n+2)) # _Chai Wah Wu_, Jan 23 2025

