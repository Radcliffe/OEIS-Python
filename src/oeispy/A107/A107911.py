# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A107911

def ok(n): b = bin(n)[2:]; return "00" in b and "11" in b
print([k for k in range(153) if ok(k)]) # _Michael S. Branicky_, Dec 19 2021

