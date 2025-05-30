# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A338524

from sympy import prime
def A338524(n):
    k = prime(n)
    m = k>>1
    while m > 0:
        k ^= m
        m >>= 1
    return k # _Chai Wah Wu_, Jun 29 2022

