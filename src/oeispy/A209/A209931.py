# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A209931

from sympy import divisors
def ok(n): return all('0' not in str(d) for d in divisors(n, generator=True))
print([k for k in range(1, 112) if ok(k)]) # _Michael S. Branicky_, Jul 01 2025

