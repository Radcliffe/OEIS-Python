# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362605

from sympy import factorint
def ok(n): return n>1 and (e:=list(factorint(n).values())).count(max(e))>1
print([k for k in range(155) if ok(k)]) # _Michael S. Branicky_, May 06 2023

