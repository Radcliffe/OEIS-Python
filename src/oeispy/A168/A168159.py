# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A168159

from sympy import isprime
def c(n): return isprime(n) and isprime(int(str(n)[::-1]))
def a(n): return next(p-10**(n-1) for p in range(10**(n-1), 10**n) if c(p))
print([a(n) for n in range(1, 56)]) # _Michael S. Branicky_, Jun 27 2022

