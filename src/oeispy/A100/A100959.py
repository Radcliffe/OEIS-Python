# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A100959

from math import isqrt
from sympy import prime, primepi
def A100959(n):
    def f(x): return n+int(sum(primepi(x//prime(k))-k+1 for k in range(1,primepi(isqrt(x))+1)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Jul 23 2024

