# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384955

from math import factorial, prod
def a(n): return factorial(sum(digits:=list(map(int, str(n))))) // prod(factorial(x) for x in digits)
print([a(n) for n in range(70)]) # _David Radcliffe_, Jun 15 2025

