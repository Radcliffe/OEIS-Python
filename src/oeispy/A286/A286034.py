# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A286034

from sympy import factorint, divisors, divisor_sigma
def T(n, m): return ((n + m)**2 - n - 3*m + 2)/2
def P(n):
    f = factorint(n)
    return sorted([f[i] for i in f])
def a046523(n):
    x=1
    while True:
        if P(n) == P(x): return x
        else: x+=1
def a000265(n): return max(list(filter(lambda i: i%2 == 1, divisors(n))))
def a161942(n): return a000265(divisor_sigma(n))
def a(n): return T(a046523(n), a161942(n)) # _Indranil Ghosh_, May 07 2017

