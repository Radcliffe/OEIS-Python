# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A131605

from sympy import mobius, integer_nthroot, primepi
def A131605(n):
    def f(x): return int(n-2+x+sum(mobius(k)*((a:=integer_nthroot(x,k)[0])-1)+primepi(a) for k in range(2,x.bit_length())))
    kmin, kmax = 1,2
    while f(kmax) >= kmax:
        kmax <<= 1
    while True:
        kmid = kmax+kmin>>1
        if f(kmid) < kmid:
            kmax = kmid
        else:
            kmin = kmid
        if kmax-kmin <= 1:
            break
    return kmax # _Chai Wah Wu_, Aug 14 2024

