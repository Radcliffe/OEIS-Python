# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A289440

from sympy import divisors, floor, gcd
def a(n): return n*max([(floor((d - 1 - gcd(d, 3))/5) + 1)/d for d in divisors(n)])
print([a(n) for n in range(2, 101)]) # _Indranil Ghosh_, Jul 08 2017

