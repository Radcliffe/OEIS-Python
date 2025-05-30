# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A179698

from sympy import primepi, primerange, integer_nthroot
def A179698(n):
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
    def f(x): return n+x-sum(primepi(x//(p**4*q**3)) for p in primerange(integer_nthroot(x,4)[0]+1) for q in primerange(integer_nthroot(x//p**4,3)[0]+1))+sum(primepi(integer_nthroot(x//p**4,4)[0]) for p in primerange(integer_nthroot(x,4)[0]+1))+sum(primepi(integer_nthroot(x//p**5,3)[0]) for p in primerange(integer_nthroot(x,5)[0]+1))+sum(primepi(x//p**7) for p in primerange(integer_nthroot(x,7)[0]+1))-(primepi(integer_nthroot(x,8)[0])<<1)
    return bisection(f,n,n) # _Chai Wah Wu_, Mar 28 2025

