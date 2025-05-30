# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A291302

from sympy import primorial, isprime, divisor_sigma
def A291302(n):
    m, c = primorial(n), 0
    while not isprime(m):
        m = divisor_sigma(m) - 1
        c += 1
    return c # _Chai Wah Wu_, Aug 31 2017

