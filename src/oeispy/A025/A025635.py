# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A025635

from sympy import integer_log
def A025635(n):
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
    def f(x): return n+x-sum(integer_log(x//10**i,9)[0]+1 for i in range(integer_log(x,10)[0]+1))
    return bisection(f,n,n) # _Chai Wah Wu_, Mar 25 2025

