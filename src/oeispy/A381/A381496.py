# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381496

from math import isqrt
from sympy import primepi, integer_nthroot, mobius
def A381496(n):
    def squarefreepi(n): return int(sum(mobius(k)*(n//k**2) for k in range(1, isqrt(n)+1)))
    m, l = 10**n, 0
    j, c = isqrt(m), -1-sum(primepi(integer_nthroot(m,k)[0]) for k in range(2,m.bit_length())),
    while j>1:
        k2 = integer_nthroot(m//j**2,3)[0]+1
        w = squarefreepi(k2-1)
        c += j*(w-l)
        l, j = w, isqrt(m//k2**3)
    return c+squarefreepi(integer_nthroot(m,3)[0])-l # _Chai Wah Wu_, Feb 25 2025

