# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346041

from sympy import factorint
def ok(n):
    f = factorint(n); w = len(f); W = sum(f.values())
    return (w == 1 and W >= 2) or (w == 2 and W == 2)
print(list(filter(ok, range(170)))) # _Michael S. Branicky_, Jul 03 2021

