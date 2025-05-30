# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365649

from sympy import divisors, primefactors, prod, reduced_totient, divisor_sigma
def psi(n):
    return n*prod(p+1 for p in primefactors(n))//prod(primefactors(n))
def a(n): return sum(divisor_sigma(d, 1) * psi(n//d) for d in divisors(n))

