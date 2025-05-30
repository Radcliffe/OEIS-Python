# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356018

from sympy import divisors
def c(n): return bin(n).count("1")&1 == 0
def a(n): return sum(1 for d in divisors(n, generator=True) if c(d))
print([a(n) for n in range(1, 101)]) # _Michael S. Branicky_, Jul 23 2022

