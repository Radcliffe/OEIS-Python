# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A255398

def ok(k): return "1" not in str(k**2)
print([k for k in range(160) if ok(k)]) # _Michael S. Branicky_, Apr 27 2023

