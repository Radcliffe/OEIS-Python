# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A136399

def ok(n): return any(d > '1' for d in str(n))
print([k for k in range(76) if ok(k)]) # _Michael S. Branicky_, Oct 29 2024

