# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376800

from sympy import factorint
def ok(n):
    f = factorint(n)
    return len(f) == sum(f.values()) == 3 and len(set([len(str(p)) for p in f])) == 1
print([k for k in range(9300) if ok(k)]) # _Michael S. Branicky_, Oct 05 2024

