# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A098592

from sympy import primerange
def a(n): return len(list(primerange(n*30, (n+1)*30)))
print([a(n) for n in range(106)]) # _Michael S. Branicky_, Oct 07 2021

