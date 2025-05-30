# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A378081

from sympy import isprime
from itertools import combinations as C
def ok(n):
    if n < 100 or not isprime(n): return False
    s = str(n)
    return all(isprime(int(t)) for i, j in C(range(len(s)), 2) if (t:=s[:i]+s[i+1:j]+s[j+1:])!="")
print([k for k in range(1, 10**6) if ok(k)]) # _Michael S. Branicky_, Nov 15 2024

