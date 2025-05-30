# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A260985

from sympy import isprime, primefactors
def omega(n): return 0 if n==1 else len(primefactors(n))
def bigomega(n): return 0 if n==1 else bigomega(n//min(primefactors(n))) + 1
def ok(n):
    d = bigomega(n) - omega(n)
    return d%2 and isprime(d)
print([n for n in range(1, 1001) if ok(n)]) # _Indranil Ghosh_, Apr 25 2017

