# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A169966

def a(n): return 3*int(bin(n)[2:])
print([a(n) for n in range(40)]) # _Michael S. Branicky_, Mar 30 2021

