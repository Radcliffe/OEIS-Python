# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A106151

def a(n): return int(bin(n).replace("b", "").replace("10", "1"), 2)
print([a(n) for n in range(1, 78)]) # _Michael S. Branicky_, Nov 12 2021

