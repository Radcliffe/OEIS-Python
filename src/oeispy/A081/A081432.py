# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A081432

def a(n): return int(str(int(bin(n)[:1:-1], 2))[::-1])
print([a(n) for n in range(75)]) # _Michael S. Branicky_, Jan 30 2023

