# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A285879

from sympy.ntheory.factor_ import core
def a(n): return sum([1 for k in range(1, n + 1) if k%2==1 and core(k)==k]) # _Indranil Ghosh_, Apr 28 2017

