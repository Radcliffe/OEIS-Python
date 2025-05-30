# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287775

from math import isqrt
def A287775(n):
    def f(x): return n+(r:=isqrt(x**2//5))+((isqrt(5*(r+1)**2)+r+1&-2)-r-1<=x)
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m # _Chai Wah Wu_, May 05 2025

