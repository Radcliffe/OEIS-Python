# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A035531

from sympy import primefactors
def a(n): return 0 if n<2 else bin(n)[2:].count("1") + len(primefactors(n)) - 1 # _Indranil Ghosh_, Apr 25 2017

