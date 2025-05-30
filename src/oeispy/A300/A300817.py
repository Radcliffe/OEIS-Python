# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A300817

from sympy import nextprime, isprime
def A300817(n):
    p, n2 = 2, n**2
    if n % 2:
        return 2 if isprime(2+n2) else 0
    while not isprime(p+n2):
        p = nextprime(p)
    return p # _Chai Wah Wu_, Mar 14 2018

