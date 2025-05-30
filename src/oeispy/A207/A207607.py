# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A207607

from sympy import Poly
from sympy.abc import x
def u(n, x): return 1 if n==1 else u(n - 1, x) + v(n - 1, x)
def v(n, x): return 1 if n==1 else x*u(n - 1, x) + (x + 1)*v(n - 1, x)
def a(n): return Poly(v(n, x), x).all_coeffs()[::-1]
for n in range(1, 13): print(a(n)) # _Indranil Ghosh_, May 28 2017

