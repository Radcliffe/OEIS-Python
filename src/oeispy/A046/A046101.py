# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046101

from sympy import mobius, integer_nthroot
def A046101(n):
    def f(x): return n+sum(mobius(k)*(x//k**4) for k in range(1, integer_nthroot(x,4)[0]+1))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 05 2024

