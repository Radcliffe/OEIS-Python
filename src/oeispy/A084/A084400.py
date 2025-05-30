# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A084400

from sympy import primepi, integer_nthroot
def A084400(n):
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
    def f(x): return n-1+x-sum(primepi(integer_nthroot(x,1<<i)[0]) for i in range(x.bit_length().bit_length()))
    return bisection(f,n,n) # _Chai Wah Wu_, Mar 25 2025

