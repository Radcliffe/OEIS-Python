# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A221220

from sympy import isprime, primefactors
def ok(n):
    pf = primefactors(n)
    if len(pf) < 2: return False
    return isprime(int("".join(str(p) for p in pf)))
print(list(filter(ok, range(2, 220)))) # _Michael S. Branicky_, Jun 12 2021

