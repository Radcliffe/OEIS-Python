# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A141642

from sympy import isprime
def ok(n): return isprime(sum(map(int, str(n)))) and not isprime(n)
print([k for k in range(237) if ok(k)]) # _Michael S. Branicky_, Dec 14 2021

