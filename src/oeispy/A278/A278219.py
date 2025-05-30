# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A278219

from sympy import prime, factorint
import math
def A(n): return n - 2**int(math.floor(math.log(n, 2)))
def b(n): return n + 1 if n<2 else prime(1 + (len(bin(n)[2:]) - bin(n)[2:].count("1"))) * b(A(n))
def a005940(n): return b(n - 1)
def P(n):
    f = factorint(n)
    return sorted([f[i] for i in f])
def a046523(n):
    x=1
    while True:
        if P(n) == P(x): return x
        else: x+=1
def a003188(n): return n^int(n/2)
def a243353(n): return a005940(1 + a003188(n))
def a(n): return a046523(a243353(n)) # _Indranil Ghosh_, May 07 2017

