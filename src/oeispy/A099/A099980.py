# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A099980

from math import isqrt
from sympy import primepi, primerange
def A099980(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return int((n<<1)+1+x+((t:=primepi(s:=isqrt(x)))*(t-1)>>1)-sum(primepi(x//p) for p in primerange(s+1)))
    return bisection(f,(n<<1)+1,(n<<1)+1) # _Chai Wah Wu_, Oct 23 2024

