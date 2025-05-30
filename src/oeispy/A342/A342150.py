# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342150

from sympy import isprime, primerange
def ok(p): return sum(isprime(p+i*10) for i in range(1, 5)) >= 3
def aupto(lim): return [p for p in primerange(1, lim+1) if ok(p)]
print(aupto(13681)) # _Michael S. Branicky_, Mar 02 2021

