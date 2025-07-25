# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369992

from functools import cache, reduce; from sympy.abc import x; from sympy import lcm, fibonacci
@cache
def kappa(n): return (1-(n%2)*2) * Q(n).subs(x,1) if n else 1
@cache
def Q(n): return (q(n).diff() * q(n-1)).integrate()
@cache
def q(n): return (1-x if n==1 else n%2-Q(n-1)/kappa(n-1)) if n else x
def denom(c): return c.denominator if c%1 else 1
def row(n): qn = q(n); k0 = 1<<(n>>1); k1 = 1+fibonacci(n+1); dn = reduce(lcm,(denom(qn.coeff(x,k)) for k in range(k0,k1))); return [qn.coeff(x,k)*dn for k in range(k0,k1)]
for n in range(15): print(row(n))

