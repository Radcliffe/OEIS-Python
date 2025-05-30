# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A106419

from itertools import count
from math import isqrt, prod
from sympy import primerange, integer_nthroot, primepi, primorial
def A106419(n):
    if n == 1: return 97
    def g(x,a,b,c,m): yield from (((d,) for d in enumerate(primerange(b+1,isqrt(x//c)+1),a+1)) if m==2 else (((a2,b2),)+d for a2,b2 in enumerate(primerange(b+1,integer_nthroot(x//c,m)[0]+1),a+1) for d in g(x,a2,b2,c*b2,m-1)))
    def f(x): return int(sum(primepi(x//prod(c[1] for c in a))-a[-1][0] for a in g(x,0,1,1,n)))
    for l in count(len(str(primorial(n)))-1):
        kmin, kmax = 9*10**l-1, 10**(l+1)-1
        mmin, mmax = f(kmin), f(kmax)
        if mmax>mmin:
            while kmax-kmin > 1:
                kmid = kmax+kmin>>1
                mmid = f(kmid)
                if mmid > mmin:
                    kmax, mmax = kmid, mmid
                else:
                    kmin, mmin = kmid, mmid
            return kmax # _Chai Wah Wu_, Aug 29 2024

