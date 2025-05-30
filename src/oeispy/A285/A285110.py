# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A285110

from operator import mul
from sympy import prime, primefactors
from functools import reduce
def a001222(n): return 0 if n<2 else a001222(n//min(primefactors(n))) + 1
def a019565(n): return reduce(mul, (prime(i+1) for i, v in enumerate(bin(n)[:1:-1]) if v == '1')) if n > 0 else 1 # This function from _Chai Wah Wu_
def a007947(n): return 1 if n<2 else reduce(mul, primefactors(n))
def a065642(n):
    if n==1: return 1
    r=a007947(n)
    n += r
    while a007947(n)!=r:
        n+=r
    return n
def a285323(n): return a065642(a065642(a019565(n)))//a019565(n)
def a(n): return a001222(a285323(n))
print([a(n) for n in range(121)]) # _Indranil Ghosh_, Apr 20 2017

