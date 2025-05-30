# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A216426

from math import isqrt
from sympy import integer_nthroot, mobius, primepi
def A216426(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x):
        j, b, a, d = isqrt(x), integer_nthroot(x,6)[0], integer_nthroot(x,5)[0], integer_nthroot(x,10)[0]
        l, c = 0, n+x-2+primepi(b)+sum(mobius(k)*(j//k**3) for k in range(d+1, b+1))+primepi(d)+sum(mobius(k)*(a//k**2+j//k**3) for k in range(1, d+1))
        while j>1:
            k2 = integer_nthroot(x//j**2,3)[0]+1
            w = sum(mobius(k)*((k2-1)//k**2) for k in range(1, isqrt(k2-1)+1))
            c -= j*(w-l)
            l, j = w, isqrt(x//k2**3)
        return c+l
    return bisection(f,n,n) # _Chai Wah Wu_, Sep 13 2024

