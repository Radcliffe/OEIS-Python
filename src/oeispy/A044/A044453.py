# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A044453

from sympy.ntheory.factor_ import digits
def has23(n): return "23" in "".join(map(str, digits(n, 4)[1:]))
def ok(n): return has23(n) and not has23(n+1)
print([k for k in range(972) if ok(k)]) # _Michael S. Branicky_, Nov 27 2021

