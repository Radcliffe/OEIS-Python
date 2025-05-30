# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A284620

from math import isqrt
def A130568(n): return (n+isqrt(5*n**2)&-2)|1
def A284620(n):
    def bsearch(f, n):
        kmin, kmax = 0, 1
        while f(kmax) <= n:
            kmax <<= 1
        kmin = kmax>>1
        while True:
            kmid = kmax+kmin>>1
            if f(kmid) > n:
                kmax = kmid
            else:
                kmin = kmid
            if kmax-kmin <= 1:
                break
        return kmin
    return (2 if n>1 and A130568(bsearch(A130568,n))==n else 0) if n&1 else 1 # _Chai Wah Wu_, May 22 2025

