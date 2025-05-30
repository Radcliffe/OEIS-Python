# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A076405

from math import gcd
from sympy import mobius, integer_nthroot, factorint
def A076405(n):
    if n == 1: return 1
    def f(x): return int(n-2+x+sum(mobius(k)*(integer_nthroot(x,k)[0]-1) for k in range(2,x.bit_length())))
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
    return kmax*integer_nthroot(kmax, gcd(*factorint(kmax).values()))[0] # _Chai Wah Wu_, Aug 13 2024

