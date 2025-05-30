# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354747

from sympy import isprime
def f(x): return 3*x + 2
def a(n):
    fn, c = f(2*n-1), 1
    while not isprime(fn): fn, c = f(fn), c+1
    return c
print([a(n) for n in range(1, 88)]) # _Michael S. Branicky_, Jun 06 2022

