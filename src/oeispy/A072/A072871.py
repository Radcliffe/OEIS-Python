# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A072871

from sympy import npartitions
def a(n):
    k = 1
    while npartitions(k)%n: k += 1
    return npartitions(k)
print([a(n) for n in range(1, 48)]) # _Michael S. Branicky_, Aug 05 2022

