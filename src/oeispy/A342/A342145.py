# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342145

def ok(n): return set(str(2*n+1)) & set(str(n)+str(n+1)) != set()
print([k for k in range(111) if ok(k)]) # _Michael S. Branicky_, Oct 24 2021

