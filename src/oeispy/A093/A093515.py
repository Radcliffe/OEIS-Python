# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A093515

from sympy import isprime
def ok(n): return isprime(n) or isprime(n-1)
print(list(filter(ok, range(140)))) # _Michael S. Branicky_, Aug 10 2021

