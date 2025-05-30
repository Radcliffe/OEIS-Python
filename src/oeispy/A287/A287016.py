# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287016

from sympy import primepi, divisors
from sympy.ntheory.primetest import is_square
def A287016(n):
    if n == 1: return 0
    m, k = n, primepi(n) + n + (n>>1)
    while m != k:
        m, k = k, primepi(k) + n + (k>>1)
    return 0 if is_square(int(m)) else -(d:=divisors(m))[l:=(len(d)>>1)-1]+d[l+1]>>1 # _Chai Wah Wu_, Aug 02 2024

