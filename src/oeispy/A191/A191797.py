# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A191797

from sympy import binomial, fibonacci
def a(n): return binomial(fibonacci(n), 2) # _Indranil Ghosh_, Mar 26 2017

