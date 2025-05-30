# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A306044

from sympy import integer_log
def A306044(n):
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
    def f(x): return n+x-x.bit_length()-integer_log(x,3)[0]-integer_log(x,5)[0]
    return bisection(f,n,n) # _Chai Wah Wu_, Feb 05 2025

