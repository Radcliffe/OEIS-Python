# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A189987

from sympy import primepi, primerange, integer_nthroot
def A189987(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        kmin = kmax >> 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return n+x-sum(primepi(x//p**6) for p in primerange(integer_nthroot(x,6)[0]+1))+primepi(integer_nthroot(x,7)[0])
    return bisection(f,n,n) # _Chai Wah Wu_, Feb 22 2025

