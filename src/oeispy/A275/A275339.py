# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A275339

from functools import cache
from sympy import factorint
@cache
def WaterCapacity(N: int) -> int:
    if N < 2: return 0
    x: list[int] = [p**e for p, e in factorint(N).items()]
    n = len(x); wc = 0
    left  = [0] * n;  left[0]  = x[0]
    right = [0] * n; right[n-1] = x[n-1]
    for k in range(n): left[k] = max(left[k - 1], x[k])
    for k in range(n - 2, -1, -1): right[k] = max(right[k + 1], x[k])
    for k in range(n): wc += min(left[k], right[k]) - x[k]
    return wc
def a(n: int) -> int:
    j = 1
    while True:
        if WaterCapacity(j) == n: return j
        j += 1
print([a(n) for n in range(1, 20)])  # _Peter Luschny_, Dec 16 2024

