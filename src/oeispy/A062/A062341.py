# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062341

from sympy import primerange as primes
def ok(p): return sum(map(int, str(p))) == 5
print(list(filter(ok, primes(1, 202002)))) # _Michael S. Branicky_, May 23 2021

