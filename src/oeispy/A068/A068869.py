# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068869

from math import factorial, isqrt
def a(n): return (isqrt((f:=factorial(n))-1)+1)**2 - f
print([a(n) for n in range(1, 30)]) # _Michael S. Branicky_, Jan 30 2023

