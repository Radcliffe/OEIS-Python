# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A285551

from sympy import binomial
def A(n): return sum([binomial(k, n - 2*k) for k in range(int(n/2) + 1)])
def a000931(n): return 1 if n==0 else 0 if n<3 else A(n - 3)
def a(n): return a000931(n + 5)**2*a000931(n + 6) # _Indranil Ghosh_, Apr 26 2017

