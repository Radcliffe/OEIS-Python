# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A331835

from sympy import prime
def p(n): return prime(n) if n >= 1 else 1
def a(n): return sum(p(i)*int(b) for i, b in enumerate(bin(n)[:1:-1]))
print([a(n) for n in range(69)]) # _Michael S. Branicky_, Jun 13 2021

