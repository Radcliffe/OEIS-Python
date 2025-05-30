# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349824

from sympy import factorint
def a(n):
    if n == 0: return 0
    f = factorint(n)
    return sum(f.values()) * sum(p*e for p, e in f.items())
print([a(n) for n in range(74)]) # _Michael S. Branicky_, Jan 02 2022

