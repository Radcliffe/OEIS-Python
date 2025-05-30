# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A162022

from sympy import primepi, primefactors
def A162022(n):
    if n == 1: return 3
    m, k = n, primepi(n) + n + (n>>1)
    while m != k:
        m, k = k, primepi(k) + n + (k>>1)
    return min(primefactors(m)) # _Chai Wah Wu_, Jul 31 2024

