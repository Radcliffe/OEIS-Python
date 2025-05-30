# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A242118

from sympy import factorint
def a(n):
    r = 1
    for p, e in factorint(n).items():
        if p%4 == 1: r *= 2*e + 1
    return 8*n - 4*r if n > 0 else 0

