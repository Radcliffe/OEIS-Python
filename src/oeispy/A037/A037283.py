# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A037283

from sympy import divisors
def a(n): return int("".join(str(d) for d in divisors(n) if d%2==1))
print([a(n) for n in range(1, 52)]) # _Michael S. Branicky_, Dec 31 2020

