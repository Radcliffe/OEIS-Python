# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A097312

from sympy import isprime
def ok(n): s = str(n); return isprime(int(s[1:]+s[0]))
print([k for k in range(171) if ok(k)]) # _Michael S. Branicky_, May 08 2023

