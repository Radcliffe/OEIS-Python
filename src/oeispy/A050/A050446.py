# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A050446

from functools import cache
@cache
def T(n, k):
    return T(n, k - 1) + sum(T(2 * j, k - 1) * T(n - 1 - 2 * j, k)
        for j in range(1 + (n - 1) // 2)) if k > 0 else 1
for n in range(6): print([T(n - k, k) for k in range(n + 1)])
# _Peter Luschny_, Jun 08 2024

