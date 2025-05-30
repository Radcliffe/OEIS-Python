# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374433

from math import prod
from sympy import primefactors
def PF(n): return set(primefactors(n)) if n > 0 else set({})
def PrimeIntersect(n, k): return prod(PF(n).intersection(PF(k)))
def PrimeSymDiff(n, k): return prod(PF(n).symmetric_difference(PF(k)))
def PrimeUnion(n, k): return prod(PF(n).union(PF(k)))
def PrimeDiff(n, k): return prod(PF(n).difference(PF(k)))
A374433 = PrimeIntersect; A374434 = PrimeSymDiff
A374435 = PrimeDiff; A374436 = PrimeUnion
for n in range(11): print([A374433(n, k) for k in range(n + 1)])

