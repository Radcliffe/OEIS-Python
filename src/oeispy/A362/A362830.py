# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362830

from sympy.ntheory import digits
def c(v): return all(v[i+1] > v[i] for i in range(len(v)-1))
def a(n): return sum(1 for b in range(2, n) if c(digits(n, b)[1:]))
print([a(n) for n in range(1, 71)]) # _Michael S. Branicky_, May 05 2023

