# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A056170

from sympy import factorint
def a(n):
    f = factorint(n)
    return sum([1 for i in f if f[i]!=1]) # _Indranil Ghosh_, Apr 24 2017

