# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349904

# After the Maple program of _Alois P. Heinz_.
from functools import cache
from math import comb
def binomial(n, k):
    if n == -1: return 1
    return comb(n, k)
@cache
def A000073(n):
    if n <= 1: return 0
    if n == 2: return 1
    return A000073(n-1) + A000073(n-2) + A000073(n-3)
@cache
def b(n, i):
    if n == 0: return 1
    if i <  1: return 0
    return sum(binomial(a(i) + j - 1, j) *
               b(n - i * j, i - 1) for j in range(1 + n // i))
@cache
def a(n): return (A000073(n - 1) - b(n, n - 1))
print([a(n) for n in range(1, 41)])

