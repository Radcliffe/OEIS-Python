# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379929

from sympy import primeomega
def ok(n): return primeomega(n) == len(s:=str(n)) - sum(1 for i in range(1, len(s)) if s[i-1] == s[i])
print([k for k in range(1, 232) if ok(k)]) # _Michael S. Branicky_, Jan 08 2025

