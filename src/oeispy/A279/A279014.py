# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A279014

from sympy import binomial, fibonacci
def a(n): return sum([fibonacci(k + 1)*binomial(2*n - 1, n - k) for k in range(n + 1)])
print([a(n) for n in range(24)]) # _Indranil Ghosh_, Jun 30 2017

