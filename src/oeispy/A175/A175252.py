# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A175252

from sympy import divisors
def ok(n):
    target, s = str(n), ""
    if target[0] != "1": return False
    for d in divisors(n):
        s += str(d)
        if len(s) >= len(target): return s == target
        elif not target.startswith(s): return False
print([k for k in range(10**6) if ok(k)]) # _Michael S. Branicky_, Sep 22 2022

