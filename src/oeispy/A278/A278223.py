# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A278223

from sympy import factorint
def P(n):
    f = factorint(n)
    return sorted([f[i] for i in f])
def a046523(n):
    x=1
    while True:
        if P(n) == P(x): return x
        else: x+=1
def a(n): return a046523(2*n - 1) # _Indranil Ghosh_, May 11 2017

