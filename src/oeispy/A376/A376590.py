# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376590

from math import isqrt
from sympy import mobius
def A376590(n):
    def iterfun(f,n=0):
        m, k = n, f(n)
        while m != k: m, k = k, f(k)
        return m
    def f(x): return n+x-sum(mobius(k)*(x//k**2) for k in range(1, isqrt(x)+1))
    a = iterfun(f,n)
    b = iterfun(lambda x:f(x)+1,a)
    return a+iterfun(lambda x:f(x)+2,b)-(b<<1) # _Chai Wah Wu_, Oct 02 2024

