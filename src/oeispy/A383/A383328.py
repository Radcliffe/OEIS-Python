# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383328

def ok(n): return set(s:=str(n)) == set(str(sum(int(d)**2 for d in s)))
print([k for k in range(10**4) if ok(k)]) # _Michael S. Branicky_, Apr 23 2025

