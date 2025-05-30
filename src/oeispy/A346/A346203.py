# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346203

from sympy import nextprime
def A346203(n):
    m, k, p, s = 1, 0, 1, str(n)
    while s not in str(m):
        k += 1
        p = nextprime(p)
        m *= p
    return k # _Chai Wah Wu_, Jul 12 2021

