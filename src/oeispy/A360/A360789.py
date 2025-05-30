# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360789

from sympy import prime, nextprime
def A360789(n):
    p, m = prime(n+1), n+1
    while p%m != n:
        p = nextprime(p)
        m += 1
    return p # _Chai Wah Wu_, Mar 18 2023

