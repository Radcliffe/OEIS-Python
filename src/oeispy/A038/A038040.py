# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A038040

from sympy import divisor_count as d
def a(n): return n*d(n)
print([a(n) for n in range(1, 60)]) # _Michael S. Branicky_, Mar 15 2022

