# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055241

from sympy.ntheory import digits
def a(n): return next((b for b in range(3, n-2) if not any(n%d==0 for d in digits(n, b)[1:] if d > 0)), 0)
print([a(n) for n in range(1, 91)]) # _Michael S. Branicky_, Oct 29 2024

