# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363393

from functools import cache
@cache
def T(n: int, k: int) -> int:
    if k == 0: return 1
    if k % 2 == 0:  return 0
    if k == n: return 1 - sum(T(n, j) for j in range(1, n, 2))
    return (T(n - 1, k) * n) // (n - k)
for n in range(10): print([T(n, k) for k in range(n + 1)])

