# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362792

def ok(n): return set(str(3*n)) == set(str(7*n))
print([k for k in range(11000) if ok(k)]) # _Michael S. Branicky_, May 04 2023

