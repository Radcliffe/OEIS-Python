# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A097961

from sympy import sieve
L = sieve.primerange(3, 1.7*10**11); s, k = 0, 0
for p in L:
    s += p;  k += 1
if s%k == 0: print(k, end = ", ")  # _Ya-Ping Lu_, Jun 16 2023

