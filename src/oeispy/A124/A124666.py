# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A124666

from sympy import isprime
def ok(n):
    s = str(n)
    if s[-1] not in "1379": return False
    if any(isprime(int(s+c)) for c in "1379"): return False
    return not any(isprime(int(c+s)) for c in "0123456789")
print([k for k in range(7114) if ok(k)]) # _Michael S. Branicky_, Aug 02 2022

