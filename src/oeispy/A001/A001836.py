# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001836

from sympy import totient
def ok(n): return totient(2*n - 1) < totient(2*n) # _Indranil Ghosh_, Apr 29 2017

