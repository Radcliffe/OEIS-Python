# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A072214

from sympy import npartitions as p, fibonacci as f
def a(n): return p(f(n)) # _Indranil Ghosh_, Jun 08 2017

