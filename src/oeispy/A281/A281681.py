# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A281681

from sympy import primepi, primefactors
def A281681(n):
    if n == 1: return 1
    m, k = n, primepi(n) + n + (n>>1)
    while m != k:
        m, k = k, primepi(k) + n + (k>>1)
    return primepi(min(primefactors(m)))-1 # _Chai Wah Wu_, Aug 02 2024

