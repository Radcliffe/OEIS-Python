# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A114277

from functools import cache
@cache
def B(n, k):
    if n <= 0 or k <= 0: return 0
    if n == k: return 1
    return B(n - 1, k) + B(n, k - 1)
def A114277(n): return B(n + 5, n + 1)
print([A114277(n) for n in range(24)]) # _Peter Luschny_, May 16 2022

