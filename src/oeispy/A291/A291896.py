# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A291896

from sympy.core.cache import cacheit
@cacheit
def b(n, i): return 1 if n==0 else sum(b(n - j, j) for j in range(max(1, i - 1), min(i + 1, n) + 1))
def a(n): return b(n, 0)
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Sep 06 2017, after Maple code

