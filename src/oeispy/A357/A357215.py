# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357215

from sympy import primepi
def a(n): return 2**primepi(n) - 1
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Sep 24 2022

