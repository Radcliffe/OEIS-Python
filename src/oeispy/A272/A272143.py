# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A272143

from sympy import isprime
def a(n): return sum(1 for i in range(n-1) if isprime(2**n-1-2**i))
print([a(n) for n in range(1, 81)]) # _Michael S. Branicky_, Nov 09 2023

