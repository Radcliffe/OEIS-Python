# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046388

from math import isqrt
from sympy import primepi, primerange
def A046388(n):
    if n == 1: return 15
    def f(x): return int(n-1+x+(t:=primepi(s:=isqrt(x)))+(t*(t-1)>>1)-sum(primepi(x//k) for k in primerange(3, s+1)))
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    return bisection(f,n,n) # _Chai Wah Wu_, Sep 10 2024

