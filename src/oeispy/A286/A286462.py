# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A286462

from sympy import divisors, divisor_count, mobius
def a051064(n): return -sum([mobius(3*d)*divisor_count(n/d) for d in divisors(n)])
def v(n): return bin(n)[2:][::-1].index("1")
def a089309(n): return  0 if n==0 else v(n/2**v(n) + 1)
def T(n, m): return ((n + m)**2 - n - 3*m + 2)/2
def a(n): return T(a051064(n), a089309(n)) # _Indranil Ghosh_, May 11 2017

