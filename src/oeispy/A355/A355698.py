# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355698

from sympy import divisors
def c(n): return len(set(str(n))) == 1
def a(n): return sum(1 for d in divisors(n, generator=True) if c(d))
print([a(n) for n in range(1, 105)]) # _Michael S. Branicky_, Jul 14 2022

