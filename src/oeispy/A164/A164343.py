# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A164343

def bal(n): return n and n.bit_length() == n.bit_count() * 2
print([s for s in (k*k for k in range(403)) if bal(s)]) # _Michael S. Branicky_, Jul 12 2022

