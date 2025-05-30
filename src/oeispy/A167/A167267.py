# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A167267

# Produces the triangle when the array is read by antidiagonals
import math
from sympy import sqrt
r=(1 + sqrt(5))/2
def s(n): return 1 if n<1 else s(n - 1) + 1 + int(math.floor(n*r))
def p(n): return n + 1 + sum(int(math.floor((n - k)/r)) for k in range(n+1))
v=[s(n) for n in range(101)]
u=[p(n) for n in range(101)]
def w(i, j): return u[i - 1] + v[j - 1] + (i - 1) * (j - 1) - 1
for n in range(1, 11):
    print([w(k, n - k + 1) for k in range(1, n + 1)]) # _Indranil Ghosh_, Mar 26 2017

