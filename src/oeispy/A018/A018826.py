# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A018826

def ok(n): return bin(n)[2:] in bin(n**2)[2:]
print([k for k in range(9999) if ok(k)]) # _Michael S. Branicky_, Apr 04 2024

