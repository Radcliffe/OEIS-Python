# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341766

def a(n):
    b = s = bin(n)[2:]
    while s.find(b, 1) < 0: n += 1; s += bin(n)[2:]
    return s.find(b, 1)
print([a(n) for n in range(76)]) # _Michael S. Branicky_, Sep 16 2022

