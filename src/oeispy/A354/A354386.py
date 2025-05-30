# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354386

from sympy import factorint, isprime, nextprime
def A001414(n): return sum(p*e for p, e in factorint(n).items())
def f(p): return p + A001414(p-1) + A001414(p+1)
def a(n):
    p, count = 1, 0
    while count != n:
        p = nextprime(p)
        fp, count = f(p), 1
        while isprime(fp): fp = f(fp); count += 1
    return p
print([a(n) for n in range(1, 6)]) # _Michael S. Branicky_, May 29 2022

