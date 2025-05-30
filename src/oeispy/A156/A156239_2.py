# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A156239

# faster version using octagonal structure
from sympy import primefactors, primorial
def A000567(n): return n*(3*n-2)
def A000567_distinct_factors(n):
    return len(set(primefactors(n)) | set(primefactors(3*n-2)))
def a(n):
    k, lb = 1, primorial(n)
    while A000567(k) < lb: k += 1
    while A000567_distinct_factors(k) != n: k += 1
    return A000567(k)
print([a(n) for n in range(1, 10)]) # _Michael S. Branicky_, Aug 21 2021

