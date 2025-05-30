# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377483

from sympy import nextprime, primepi
def A377483(n):
    p, k, a = nextprime(n-1), primepi(n-1)+1, bin(n)[2:]
    while True:
        if a in bin(p)[2:]:
            return k
        p = nextprime(p)
        k += 1 # _Chai Wah Wu_, Nov 20 2024

