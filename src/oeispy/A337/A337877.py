# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A337877

from sympy import primepi, primerange, integer_nthroot
def A337877(n):
    def f(x): return int(n+x-sum(primepi(x//k**2)-a for a,k in enumerate(primerange(integer_nthroot(x,3)[0]+1))))
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    return bisection(f) # _Chai Wah Wu_, Aug 29 2024

