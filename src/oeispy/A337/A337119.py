# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A337119

from math import gcd
from sympy import isprime
def ok(n):
    if not isprime(n): return False
    return all(pow(b, n-1, n-1) == 1 for b in range(2, n) if gcd(b, n-1)==1)
print([k for k in range(2594) if ok(k)]) # _Michael S. Branicky_, Apr 02 2022

