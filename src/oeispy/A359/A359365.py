# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359365

from functools import cache
from sympy import lcm
def A359365 (n: int) -> int:
    @cache
    def l(n: int) -> list[int]:
        if n == 0: return [1]
        row: list[int] = l(n - 1) + [1]
        row[0] = 0
        for k in range(n - 1, 0, -1):
            row[k] = row[k] * (n + k - 1) + row[k - 1]
        return row
    return lcm(l(n)[1:])
print([A359365(n) for n in range(21)])

