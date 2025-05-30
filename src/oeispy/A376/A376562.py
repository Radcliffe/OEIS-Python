# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376562

from itertools import count
from sympy import mobius, integer_nthroot, perfect_power
def A376562(n):
    def f(x): return int(n+1-sum(mobius(k)*(integer_nthroot(x, k)[0]-1) for k in range(2, x.bit_length())))
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    r = m+((k:=next(i for i in count(1) if not perfect_power(m+i)))<<1)
    return next(i for i in count(1-k) if not perfect_power(r+i)) # _Chai Wah Wu_, Oct 02 2024

