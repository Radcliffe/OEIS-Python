# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356791

from sympy import isprime
def ok(n):
    r = int(str(n)[::-1])
    return r > n and isprime(n) and isprime(r) and isprime(r%n)
print([k for k in range(10**5) if ok(k)]) # _Michael S. Branicky_, Sep 18 2022

