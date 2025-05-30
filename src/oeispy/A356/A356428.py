# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356428

from sympy import factorint
def gpf(n): return 1 if n == 1 else max(factorint(n))
def a(n):
    s = set()
    while n != 0: g = gpf(n); s.add(g); n = n - g
    return len(s - {1})
print([a(n) for n in range(92)]) # _Michael S. Branicky_, Aug 08 2022

