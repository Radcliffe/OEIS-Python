# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349273

from sympy import divisors, prime
def a(n): return sum(d%2 for d in divisors(prime(n)-1))
print([a(n) for n in range(1, 96)]) # _Michael S. Branicky_, Jul 04 2021

