# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A283880

from functools import cache
@cache
def a(n):
    if n <= 0: return 0
    if n <= 9: return [12, 6, 4, 6, 1, 6, 12, 10, 4][n-1]
    return a(n - a(n-1)) + a(n - a(n-2))
print([a(n) for n in range(1, 76)]) # _Michael S. Branicky_, Dec 06 2021

