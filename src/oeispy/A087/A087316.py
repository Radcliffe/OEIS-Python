# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A087316

from sympy import prime
def a(n): return sum(prime(k)**prime(n-k+1) for k in range(1, n+1))
print([a(n) for n in range(1, 16)]) # _Michael S. Branicky_, Apr 17 2021

