# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367974

from sympy import factorint
def ok(n):
    s = str(n)
    return all(str(e)+str(p) in s for p, e in factorint(n).items())
print([k for k in range(10**5) if ok(k)]) # _Michael S. Branicky_, Dec 08 2023

