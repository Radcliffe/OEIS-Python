# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A088530

from sympy import primefactors, Integer
def bigomega(n): return 0 if n==1 else bigomega(Integer(n)/primefactors(n)[0]) + 1
def omega(n): return Integer(len(primefactors(n)))
def a(n): return (bigomega(n)/omega(n)).denominator
print([a(n) for n in range(2, 51)]) # _Indranil Ghosh_, Jul 13 2017

