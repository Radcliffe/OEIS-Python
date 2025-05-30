# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359760

from functools import cache
@cache
def K(n: int, k: int) -> int:
    if k %  2: return 0
    if n <  3: return 1
    if n == k: return K(n - 1, n - 2)
    return (K(n - 1, k) * n) // (n - k)
for n in range(10): print([K(n, k) for k in range(n + 1)])

