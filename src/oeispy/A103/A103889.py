# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A103889

def a(n): return n+1 if n&1 else n-1
print([a(n) for n in range(1, 73)]) # _Michael S. Branicky_, May 03 2023

