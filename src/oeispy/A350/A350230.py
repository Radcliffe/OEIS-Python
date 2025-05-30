# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350230

from sympy import divisors, isprime
def ok(n):
    divs = divisors(n)
    if n == 0: return False
    return all(isprime(a*b+a+b) for a, b in ((d, n//d) for d in divs))
print([k for k in range(427) if ok(k)]) # _Michael S. Branicky_, Dec 21 2021

