# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A236366

from sympy.ntheory import digits
def c(n, b): d = digits(n, b)[1:]; return d == d[::-1]
def a(n): return int("0"+"".join(d for d in "23456789" if c(n, int(d))))
print([a(n) for n in range(1, 66)]) # _Michael S. Branicky_, Sep 21 2022

