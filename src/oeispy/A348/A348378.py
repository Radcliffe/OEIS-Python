# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348378

from functools import cache
@cache
def a(n): return 1 if n == 1 else 2 + sum(a(i) for i in range(1, n)) + sum(a(i) for i in range(2, n) if n%i == 0)
print([a(n) for n in range(1, 35)]) # _Michael S. Branicky_, Jan 25 2022

