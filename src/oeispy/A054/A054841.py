# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A054841

from sympy import factorint, primepi
def a(n): return sum(e*10**(primepi(p)-1) for p, e in factorint(n).items())
print([a(n) for n in range(1, 41)]) # _Michael S. Branicky_, Mar 17 2024

