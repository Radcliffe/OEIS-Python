# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340316

from math import prod, isqrt
from sympy import prime, primerange, integer_nthroot, primepi
def A340316_T(n,k):
    if n == 1: return prime(k)
    def g(x,a,b,c,m): yield from (((d,) for d in enumerate(primerange(b+1,isqrt(x//c)+1),a+1)) if m==2 else (((a2,b2),)+d for a2,b2 in enumerate(primerange(b+1,integer_nthroot(x//c,m)[0]+1),a+1) for d in g(x,a2,b2,c*b2,m-1)))
    def f(x): return int(k+x-sum(primepi(x//prod(c[1] for c in a))-a[-1][0] for a in g(x,0,1,1,n)))
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    return bisection(f) # _Chai Wah Wu_, Aug 31 2024

