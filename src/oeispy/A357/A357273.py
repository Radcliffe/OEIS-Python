# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357273

from sympy import divisors
def ok(n): return "".join(str(d) for d in divisors(n)).startswith(str(n))
print([k for k in range(10**5) if ok(k)]) # _Michael S. Branicky_, Sep 22 2022

