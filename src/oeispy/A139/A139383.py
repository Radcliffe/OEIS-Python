# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A139383

from sympy.core.cache import cacheit
from sympy import binomial
@cacheit
def A(n, k): return 1 if n==0 or k==0 else sum(binomial(n - 1, j - 1)*A(j, k - 1)*A(n - j, k) for j in range(1, n + 1))
def a(n): return A(n, n - 1)
print([a(n) for n in range(21)]) # _Indranil Ghosh_, Aug 07 2017, after Maple code

