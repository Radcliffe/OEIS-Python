# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A201266

from math import isqrt
from sympy import primepi, integer_nthroot, primerange, divisors
def A201266(n):
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
    def f(x): return int(n+x+(t:=primepi(s:=isqrt(y:=integer_nthroot(x,6)[0])))+(t*(t-1)>>1)-sum(primepi(y//k) for k in primerange(1, s+1))-primepi(integer_nthroot(x,48)[0]))
    return divisors(bisection(f,n,n))[6] # _Chai Wah Wu_, Feb 22 2025

