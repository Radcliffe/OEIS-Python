# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A072443

from math import isqrt
from sympy import divisors
def ok(n): return isqrt(n)**2<n and any(sorted(str(d)) == sorted(str(n//d)) for d in divisors(n)[1:-1])
print([k for k in range(16100) if ok(k)]) # _Michael S. Branicky_, Sep 08 2024

