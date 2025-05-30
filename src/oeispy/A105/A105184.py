# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A105184

from sympy import isprime
def ok(n):
    if not isprime(n): return False
    s = str(n)
    return any(s[i]!="0" and isprime(int(s[:i])) and isprime(int(s[i:])) for i in range(1, len(s)))
print([k for k in range(1100) if ok(k)]) # _Michael S. Branicky_, Sep 01 2024

