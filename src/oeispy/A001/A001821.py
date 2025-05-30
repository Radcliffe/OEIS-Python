# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001821

from sympy.functions.combinatorial.numbers import stirling
def s(n, k): return stirling(n, k, kind=1)
def a(n): return s(n+4, 4)**2 - 2*s(n+4, 1)*s(n+4, 7) + 2*s(n+4, 2)*s(n+4, 6) - 2*s(n+4, 3)*s(n+4, 5)
print([a(n) for n in range(15)]) # _Michael S. Branicky_, Jan 30 2021

