# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A286573

from sympy import divisors, factorint
def T(n, m): return ((n + m)**2 - n - 3*m + 2)/2
def a002326(n):
    m=1
    while True:
        if (2**m - 1)%(2*n + 1)==0: return m
        else: m+=1
def a000265(n): return max(list(filter(lambda i: i%2 == 1, divisors(n))))
def a007733(n): return a002326((a000265(n) - 1)/2)
def P(n):
    f = factorint(n)
    return sorted([f[i] for i in f])
def a046523(n):
    x=1
    while True:
        if P(n) == P(x): return x
        else: x+=1
def a(n): return T(a007733(n), a046523(n)) # _Indranil Ghosh_, May 26 2017

