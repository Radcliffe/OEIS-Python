# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A085987

from math import isqrt
from sympy import primepi, primerange, integer_nthroot
def A085987(n):
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
    def f(x): return n+x+sum((t:=primepi(s:=isqrt(y:=x//r**2)))+(t*(t-1)>>1)-sum(primepi(y//k) for k in primerange(1, s+1)) for r in primerange(isqrt(x)+1))+sum(primepi(x//p**3) for p in primerange(integer_nthroot(x,3)[0]+1))-primepi(integer_nthroot(x,4)[0])
    return bisection(f,n,n) # _Chai Wah Wu_, Mar 27 2025

