# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377468

from sympy import mobius, integer_nthroot
def A377468(n):
    if n == 1: return 1
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return int(x-1+sum(mobius(k)*(integer_nthroot(x,k)[0]-1) for k in range(2,x.bit_length())))
    m = n-f(n-1)
    return bisection(lambda x:f(x)+m,n-1,n) # _Chai Wah Wu_, Nov 05 2024

