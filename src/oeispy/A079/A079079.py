# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A079079

from sympy import prime
def a(n): return (prime(n) + 1)*(prime(n + 1) + 1)/4 # _Indranil Ghosh_, Apr 26 2017

