# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357429

from sympy import divisors
from sympy.ntheory import digits
def ok(n):
    target, s = "".join(map(str, digits(n, 3)[1:])), ""
    if target[0] != "1": return False
    for d in divisors(n):
        s += "".join(map(str, digits(d, 3)[1:]))
        if len(s) >= len(target): return s == target
        elif not target.startswith(s): return False
print([k for k in range(10**5) if ok(k)]) # _Michael S. Branicky_, Oct 01 2022

