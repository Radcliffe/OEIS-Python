# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A237256

from sympy import isprime, primerange
def is_a237256(p): return all(isprime(q) for q in (p, p+2, p+8, p+12, 2*p+1, 2*p+3, 2*p+9, 2*p+13))
print(*[ p for p in primerange(10**8) if is_a237256(p)], sep=', ')
# _David Radcliffe_, May 11 2025

