# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358984

from math import isqrt
def s(n): return isqrt(n)**2 == n
def c(n): return s(n + int(str(n)[::-1]))
def a(n): return 3 if n == 1 else sum(1 for k in range(10**(n-1), 10**n) if c(k))
print([a(n) for n in range(1, 7)]) # _Michael S. Branicky_, Dec 08 2022

