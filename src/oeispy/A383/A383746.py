# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383746

from gmpy2 import digits, mpz
def ok(n): return n and sum(map(mpz, digits(n**(3*n))))%n == 0
print([k for k in range(1100) if ok(k)]) # _Michael S. Branicky_, May 08 2025

