# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A096713

from sympy import hermite, Poly, sqrt
def a(n): return Poly(hermite(n, x/sqrt(2))/2**(n/2), x).coeffs()[::-1]
for n in range(21): print(a(n)) # _Indranil Ghosh_, May 26 2017

