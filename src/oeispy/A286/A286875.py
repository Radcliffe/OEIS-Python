# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A286875

from sympy import primefactors, isprime, gcd, divisors
def a(n): return sum(d for d in divisors(n) if gcd(d, n//d)==1 and len(primefactors(d))==1 and not isprime(d))
print([a(n) for n in range(1, 109)]) # _Indranil Ghosh_, Aug 02 2017

