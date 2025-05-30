# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341700

from sympy import nextprime
def A341700(n):
    s, m = 0, nextprime(n)
    while m <= 2*n:
        s += m
        m = nextprime(m)
    return s

