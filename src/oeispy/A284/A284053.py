# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A284053

from functools import cache
@cache
def a(n):
    if n <= 0: return 0
    if n < 16:
        return [9, 20, 5, 5, 20, 9, 20, 5, 5, 20, 9, 5, 10, 10, 20][n-1]
    return a(n - a(n-1)) + a(n - a(n-2))
print([a(n) for n in range(1, 76)]) # _Michael S. Branicky_, Sep 20 2021

