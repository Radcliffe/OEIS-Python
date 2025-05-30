# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A124317

from math import isqrt
from sympy import primepi, primerange, integer_nthroot
def A124317(n):
    def f(x): return int(x-sum(primepi(x//(k*m))-b for a,k in enumerate(primerange(integer_nthroot(x,3)[0]+1)) for b,m in enumerate(primerange(k,isqrt(x//k)+1),a)))
    def g(x): return int(x+((t:=primepi(s:=isqrt(x)))*(t-1)>>1)-sum(primepi(x//k) for k in primerange(1, s+1)))
    m, k = n, f(n)+n
    while m != k:
        m, k = k, f(k)+n
    r, k = m, g(m)+m
    while r != k:
        r, k = k, g(k)+m
    return r # _Chai Wah Wu_, Aug 17 2024

