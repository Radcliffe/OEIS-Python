# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063787

def a(n): return bin(n-1).count('1') + 1
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Dec 16 2021

