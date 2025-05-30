# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064514

from sympy import integer_log
def A064514(n):
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
    def f(x): return n+x-sum(max(0,min((i<<1)+1,(x//3**i).bit_length())-i) for i in range(integer_log(x,3)[0]+1))
    return ((m:=bisection(f,n,n))-1&~m).bit_length() # _Chai Wah Wu_, Mar 26 2025

