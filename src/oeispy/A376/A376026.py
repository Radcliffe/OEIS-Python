# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376026

from sympy import isprime
def ok(n): return isprime(int(str(n+1)+str(n**2)))
print([k for k in range(10**3) if ok(k)]) # _Michael S. Branicky_, Sep 15 2024

