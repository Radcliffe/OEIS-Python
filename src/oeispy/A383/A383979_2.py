# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383979

from sympy import isprime
def a(n):
    if n < 3: return n-1
    return sum(1 for i in range(10**(n-1), 10**n, 100) for k in (11, 33, 77, 99) if isprime(i+k))
print([a(n) for n in range(1, 10)]) # _Michael S. Branicky_, May 20 2025

