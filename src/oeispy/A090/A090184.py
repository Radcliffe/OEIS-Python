# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A090184

from sympy import integer_log
def A090184(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return n+x-sum((x//3**i).bit_length() for i in range(integer_log(x,3)[0]+1))
    return ((m:=bisection(f,n,n)+2)>>1)-m//3 # _Chai Wah Wu_, Oct 22 2024

