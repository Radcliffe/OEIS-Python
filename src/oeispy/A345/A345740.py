# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345740

from sympy import factorint, nextprime, primerange
def Omega(n): return sum(e for f, e in factorint(n).items())
def a(n):
    lb = 2**n
    p = nextprime(max(lb-n, 1) - 1)
    while Omega(p+n) != n: p = nextprime(p)
    return p
print([a(n) for n in range(1, 12)]) # _Michael S. Branicky_, Aug 14 2021

