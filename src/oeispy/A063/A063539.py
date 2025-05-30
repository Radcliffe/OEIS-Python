# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063539

from math import isqrt
from sympy import primepi
def A063539(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return int(n+primepi(x//(y:=isqrt(x)))+sum(primepi(x//i)-primepi(i) for i in range(1,y)))
    return bisection(f,n,n) # _Chai Wah Wu_, Oct 05 2024

