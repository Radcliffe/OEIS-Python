# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A279512

def a(n): return 2*6**n + 3*2**n + 1
print([a(n) for n in range(23)]) # _Michael S. Branicky_, Jun 19 2021

