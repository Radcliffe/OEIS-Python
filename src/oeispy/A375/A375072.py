# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375072

from sympy import mobius, integer_nthroot
def A375072(n):
    def f(x): return n+x-sum(mobius(k)*(x//k**4-x//k**3) for k in range(1, integer_nthroot(x,4)[0]+1))+sum(mobius(k)*(x//k**3) for k in range(integer_nthroot(x,4)[0]+1, integer_nthroot(x,3)[0]+1))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 05 2024

