# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345351

from sympy import isprime
def A000217(n): return n*(n+1)//2
def A055012(n): return sum(int(d)**3 for d in str(n))
def ok(tri): return isprime(A055012(tri))
print(list(filter(ok, (A000217(n) for n in range(500))))) # _Michael S. Branicky_, Jun 15 2021

