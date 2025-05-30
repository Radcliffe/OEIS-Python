# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371149

from sympy import factorint, Rational
def A371149(n):
    f = factorint(n)
    gpf = max(f, default=None)
    a = 0
    for p in f:
        m = gpf
        v = 0
        while m >= p:
            m //= p
            v += m
        a = max(a, Rational(f[p], v))
    return a.q

