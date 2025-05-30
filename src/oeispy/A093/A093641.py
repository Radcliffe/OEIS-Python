# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A093641

from sympy import primepi
def A093641(n):
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
    def f(x): return n-1+x-sum(primepi(x>>i) for i in range(x.bit_length()))
    return bisection(f,n,n) # _Chai Wah Wu_, Feb 02 2025

