# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A133195

def a(n): q, r = divmod(3*n, 9); return int(str(r) + "9"*q)
print([a(n) for n in range(31)]) # _Michael S. Branicky_, Feb 07 2022

