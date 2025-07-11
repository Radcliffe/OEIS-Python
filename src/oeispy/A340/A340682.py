# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340682

from math import isqrt
from sympy import mobius, integer_nthroot
def A340682(n):
    def g(x): return sum(mobius(k)*(x//k**2) for k in range(1, isqrt(x)+1))
    def f(x): return int(n+x-sum(g(integer_nthroot(x,1<<e)[0])-1 for e in range(x.bit_length().bit_length())))
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m # _Chai Wah Wu_, Jun 01 2025

