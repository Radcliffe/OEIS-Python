# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068318

from math import isqrt
from sympy import primepi, primerange, factorint
def A068318(n):
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
    def f(x): return int(n+x+((t:=primepi(s:=isqrt(x)))*(t-1)>>1)-sum(primepi(x//p) for p in primerange(s+1)))
    return sum(p*e for p,e in factorint(bisection(f,n,n)).items()) # _Chai Wah Wu_, Apr 03 2025

