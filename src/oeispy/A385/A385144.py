# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385144

from sympy import isprime
def a(n): return next((t for c in "123456789" for d in "0123456789" if c!=d and isprime(t:=int(c+d*(2*n-1)+c))), -1)
print([a(n) for n in range(1, 17)]) # _Michael S. Branicky_, Jun 19 2025

