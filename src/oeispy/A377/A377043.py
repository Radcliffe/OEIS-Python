# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377043

from sympy import mobius, primepi, integer_nthroot
def A377043(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return int(n-1+x+sum(mobius(k)*(integer_nthroot(x,k)[0]-1) for k in range(2,x.bit_length())))
    def g(x): return int(n-1+x-sum(primepi(integer_nthroot(x,k)[0]) for k in range(1,x.bit_length())))
    return bisection(f,n,n)-bisection(g,n,n) # _Chai Wah Wu_, Oct 27 2024

