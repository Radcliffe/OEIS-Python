# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A134681

from sympy import divisors
def a(n): return sum(len(str(d)) for d in divisors(n, generator=True))
print([a(n) for n in range(1, 97)]) # _Michael S. Branicky_, Nov 03 2023

